from __future__ import annotations

import math
from typing import List

from src.models import CarPose, Cone, Path2D

TRACK_WIDTH = 2.0
MAX_GATE = 6.0
CLEARANCE = 0.4
PATH_LENGTH = 8.0
STEP = 0.25


def _unit(x, y, default):
    n = math.hypot(x, y)
    return default if n < 1e-9 else (x / n, y / n)


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


class PathPlanning:
    def __init__(self, car_pose: CarPose, cones: List[Cone]):
        self.car_pose = car_pose
        self.cones = cones
        self.blue = sorted((c for c in cones if c.color == 1), key=self._dist)
        self.yellow = sorted((c for c in cones if c.color == 0), key=self._dist)

    def _dist(self, cone):
        return math.hypot(cone.x - self.car_pose.x, cone.y - self.car_pose.y)

    def generatePath(self) -> Path2D:
        car = (self.car_pose.x, self.car_pose.y)
        heading = (math.cos(self.car_pose.yaw), math.sin(self.car_pose.yaw))
        nodes = self._waypoints(car, heading)
        dense = self._spline(car, heading, nodes)
        path = self._resample(dense)
        return self._keep_clear_of_cones(path)

    def _waypoints(self, car, heading):
        candidates = sorted(
            ((math.hypot(b.x - y.x, b.y - y.y), i, j)
             for i, b in enumerate(self.blue) for j, y in enumerate(self.yellow)),
            key=lambda t: t[0])
        used_b, used_y, gates = set(), set(), []
        for dist, i, j in candidates:
            if dist > MAX_GATE:
                break
            if i in used_b or j in used_y:
                continue
            used_b.add(i)
            used_y.add(j)
            gates.append((self.blue[i], self.yellow[j]))
        lone_blue = [b for i, b in enumerate(self.blue) if i not in used_b]
        lone_yellow = [y for j, y in enumerate(self.yellow) if j not in used_y]

        width = TRACK_WIDTH
        if gates:
            width = sum(math.hypot(b.x - y.x, b.y - y.y) for b, y in gates) / len(gates)

        nodes = []
        for b, y in gates:
            gx, gy = b.x - y.x, b.y - y.y
            d = _unit(gy, -gx, heading)
            nodes.append((((b.x + y.x) / 2, (b.y + y.y) / 2), d))
        gate_nodes = list(nodes)

        gate_dists = [math.hypot(n[0][0] - car[0], n[0][1] - car[1]) for n in gate_nodes]
        for line, lone, side in ((self.blue, lone_blue, -1), (self.yellow, lone_yellow, +1)):
            for c in lone:
                if len(gate_dists) >= 2 and min(gate_dists) < self._dist(c) < max(gate_dists):
                    continue
                if gate_nodes:
                    k = min(range(len(gate_nodes)),
                            key=lambda m: math.hypot(gate_nodes[m][0][0] - c.x, gate_nodes[m][0][1] - c.y))
                    gp, gd = gate_nodes[k]
                    if _dot((c.x - gp[0], c.y - gp[1]), gd) < 0:
                        # cone behind the gate: it is already passed, so it adds no waypoint.
                        # It tells the car which way this boundary runs: previous cone -> gate cone.
                        gc = gates[k][0] if side == -1 else gates[k][1]
                        nd = _unit(gc.x - c.x, gc.y - c.y, gd)
                        if _dot(nd, gd) > 0:
                            nodes[k] = (gp, nd)
                            gate_nodes[k] = (gp, nd)
                        continue
                if gate_nodes:
                    ref = min(gate_nodes,
                              key=lambda n: math.hypot(n[0][0] - c.x, n[0][1] - c.y))[1]
                else:
                    ref = heading
                t = self._boundary_direction(line, c, ref)
                left = (-t[1], t[0])
                nodes.append(((c.x + side * left[0] * width / 2,
                               c.y + side * left[1] * width / 2), t))

        nodes.sort(key=lambda n: math.hypot(n[0][0] - car[0], n[0][1] - car[1]))
        kept = []
        prev_p, prev_d = None, None
        for p, d in nodes:
            if prev_p is not None:
                chord = (p[0] - prev_p[0], p[1] - prev_p[1])
                length = math.hypot(chord[0], chord[1])
                if length < 0.2 or _dot(chord, prev_d) < -0.25 * length:
                    continue
                prev_d = _unit(chord[0], chord[1], prev_d)
            else:
                prev_d = _unit(p[0] - car[0], p[1] - car[1], d)
            kept.append((p, d))
            prev_p = p
        return kept

    @staticmethod
    def _boundary_direction(line, cone, ref):
        if len(line) < 2:
            return ref
        i = line.index(cone)
        a, b = line[max(i - 1, 0)], line[min(i + 1, len(line) - 1)]
        return _unit(b.x - a.x, b.y - a.y, ref)

    @staticmethod
    def _spline(car, heading, nodes):
        if nodes:
            first = _unit(nodes[0][0][0] - car[0], nodes[0][0][1] - car[1], heading)
        else:
            first = heading
        pts = [(car, first)] + nodes
        dense = [car]
        for (p0, d0), (p1, d1) in zip(pts, pts[1:]):
            L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
            n = max(2, int(L / 0.05))
            for k in range(1, n + 1):
                t = k / n
                h00 = 2 * t**3 - 3 * t**2 + 1
                h10 = t**3 - 2 * t**2 + t
                h01 = -2 * t**3 + 3 * t**2
                h11 = t**3 - t**2
                dense.append((
                    h00 * p0[0] + h10 * L * d0[0] + h01 * p1[0] + h11 * L * d1[0],
                    h00 * p0[1] + h10 * L * d0[1] + h01 * p1[1] + h11 * L * d1[1],
                ))
        (px, py), (dx, dy) = pts[-1]
        for k in range(1, int(PATH_LENGTH / 0.05) + 1):
            dense.append((px + dx * 0.05 * k, py + dy * 0.05 * k))
        return dense

    @staticmethod
    def _resample(poly):
        path: Path2D = []
        target, travelled = STEP, 0.0
        for (x0, y0), (x1, y1) in zip(poly, poly[1:]):
            seg = math.hypot(x1 - x0, y1 - y0)
            while seg > 1e-9 and travelled + seg >= target - 1e-9 and target <= PATH_LENGTH + 1e-9:
                f = min(1.0, (target - travelled) / seg)
                path.append((x0 + f * (x1 - x0), y0 + f * (y1 - y0)))
                target += STEP
            travelled += seg
        return path

    def _keep_clear_of_cones(self, path):
        pts = list(path)
        radius = 5
        weights = [radius + 1 - abs(k) for k in range(-radius, radius + 1)]
        for _ in range(6):
            push = []
            for x, y in pts:
                px = py = 0.0
                for c in self.cones:
                    dx, dy = x - c.x, y - c.y
                    d = math.hypot(dx, dy)
                    if d < CLEARANCE - 1e-3:
                        if d < 1e-6:
                            dx, dy, d = 0.0, 1.0, 1.0
                        px += dx / d * (CLEARANCE - d)
                        py += dy / d * (CLEARANCE - d)
                push.append((px, py))
            if not any(abs(px) + abs(py) > 0 for px, py in push):
                break
            smooth = []
            for i in range(len(pts)):
                sx = sy = wsum = 0.0
                for k, w in zip(range(-radius, radius + 1), weights):
                    j = i + k
                    if 0 <= j < len(pts):
                        sx += w * push[j][0]
                        sy += w * push[j][1]
                        wsum += w
                smooth.append((sx / wsum, sy / wsum))
            pts = [pts[0]] + [(x + sx * 1.3, y + sy * 1.3)
                              for (x, y), (sx, sy) in zip(pts[1:], smooth[1:])]
        return pts