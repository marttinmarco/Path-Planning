from __future__ import annotations

from typing import Dict, List, Tuple

from src.models import CarPose, Cone


_SCENARIOS: Dict[str, Tuple[List[Cone], CarPose]] = {
    "1": (
        [],
        CarPose(x=0.0, y=0.0, yaw=0.0),
    ),

    "2": (
        [Cone(x=1.0, y=3.0, color=1), Cone(x=1.0, y=1.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.4),
    ),

    "3": (
        [
            Cone(x=1.0, y=3.0, color=1),
            Cone(x=3.0, y=3.0, color=1),
            Cone(x=1.0, y=1.0, color=0),
            Cone(x=3.0, y=1.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=0.8),
    ),

    "4": (
        [Cone(x=4.0, y=2.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.2),
    ),

    "5": (
        [Cone(x=4.0, y=2.0, color=0), Cone(x=3.0, y=2.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.6),
    ),

    "6": (
        [
            Cone(x=4.0, y=4.0, color=1),
            Cone(x=4.0, y=2.0, color=0),
            Cone(x=3.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=2.0),
    ),

    "7": (
        [
            Cone(x=2.0, y=3.0, color=1),
            Cone(x=4.0, y=3.0, color=1),
            Cone(x=2.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=1.4),
    ),

    "8": (
        [Cone(x=3.0, y=3.0, color=1), Cone(x=5.0, y=3.0, color=1)],
        CarPose(x=0.0, y=0.0, yaw=1.8),
    ),

    "9": (
        [Cone(x=3.0, y=3.0, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.2),
    ),

    "10": (
        [Cone(x=5.0, y=3.0, color=1), Cone(x=5.0, y=2.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.6),
    ),

    "11": (
        [
            Cone(x=1.0, y=3.0, color=1),
            Cone(x=4.0, y=5.0, color=1),
            Cone(x=1.0, y=2.0, color=0),
            Cone(x=4.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=1.0),
    ),

    "12": (
        [Cone(x=5.0, y=2.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.4),
    ),

    "13": (
        [Cone(x=5.0, y=3.0, color=0), Cone(x=5.0, y=1.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.1),
    ),

    "14": (
        [
            Cone(x=3.0, y=5.0, color=1),
            Cone(x=3.0, y=2.0, color=0),
            Cone(x=5.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=5.2),
    ),

    "15": (
        [
            Cone(x=2.0, y=5.0, color=1),
            Cone(x=3.0, y=4.0, color=1),
            Cone(x=3.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=1.6),
    ),

    "16": (
        [Cone(x=0.0, y=3.0, color=1), Cone(x=2.0, y=5.0, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.2),
    ),

    "17": (
        [Cone(x=3.0, y=5.0, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.6),
    ),

    "18": (
        [Cone(x=2.0, y=4.0, color=1), Cone(x=4.0, y=3.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.0),
    ),

    "19": (
        [
            Cone(x=2.0, y=3.0, color=1),
            Cone(x=5.0, y=3.0, color=1),
            Cone(x=2.0, y=0.0, color=0),
            Cone(x=5.0, y=2.0, color=0),
        ],
        CarPose(x=0.0, y=0.0, yaw=1.4),
    ),

    "20": (
        [Cone(x=0.0, y=2.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.8),
    ),
    
        # ---- Part 2: three cones on one side of the track ----

    # 21: straight track, only 3 blue cones visible
    "21": (
        [Cone(x=1.5, y=1.0, color=1), Cone(x=3.0, y=1.0, color=1), Cone(x=4.5, y=1.0, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.0),
    ),

    # 22: straight track, only 3 yellow cones visible
    "22": (
        [Cone(x=1.5, y=-1.0, color=0), Cone(x=3.0, y=-1.0, color=0), Cone(x=4.5, y=-1.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.0),
    ),

    # 23: diagonal straight, 3 blue + 1 yellow
    "23": (
        [Cone(x=0.7, y=2.1, color=1), Cone(x=1.7, y=3.2, color=1), Cone(x=2.8, y=4.3, color=1),
         Cone(x=3.2, y=1.8, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.8),
    ),

    # 24: left curve, 3 blue on the inside + 1 yellow
    "24": (
        [Cone(x=1.1, y=1.7, color=1), Cone(x=2.1, y=3.0, color=1), Cone(x=2.5, y=4.5, color=1),
         Cone(x=2.4, y=0.2, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.3),
    ),

    # 25: right curve, 3 yellow on the inside + 1 blue
    "25": (
        [Cone(x=1.0, y=2.1, color=1),
         Cone(x=2.0, y=0.4, color=0), Cone(x=3.5, y=0.9, color=0), Cone(x=5.1, y=0.7, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.9),
    ),

    # 26: left curve, 3 yellow on the outside + 1 blue
    "26": (
        [Cone(x=0.9, y=1.8, color=1),
         Cone(x=2.4, y=0.4, color=0), Cone(x=3.4, y=1.9, color=0), Cone(x=4.0, y=3.6, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.4),
    ),

    # 27: right curve, only 3 blue cones (outside of the turn)
    "27": (
        [Cone(x=1.0, y=2.1, color=1), Cone(x=2.7, y=2.8, color=1), Cone(x=4.5, y=2.9, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.9),
    ),

    # 28: left curve, only 3 yellow cones (outside of the turn)
    "28": (
        [Cone(x=2.4, y=0.4, color=0), Cone(x=3.4, y=1.9, color=0), Cone(x=4.0, y=3.6, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.4),
    ),

    # 29: straight, 3 blue + 2 yellow (third blue has no partner)
    "29": (
        [Cone(x=0.8, y=1.6, color=1), Cone(x=2.2, y=2.3, color=1), Cone(x=3.5, y=3.0, color=1),
         Cone(x=1.8, y=-0.2, color=0), Cone(x=3.1, y=0.6, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.5),
    ),

    # 30: steep straight, 3 yellow + 2 blue (third yellow has no partner)
    "30": (
        [Cone(x=-0.2, y=2.2, color=1), Cone(x=0.3, y=3.6, color=1),
         Cone(x=1.7, y=1.5, color=0), Cone(x=2.2, y=2.9, color=0), Cone(x=2.7, y=4.3, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.2),
    ),
    
        # 31: left curve, only 3 blue cones (inside of the turn), no yellow
    "31": (
        [Cone(x=0.6, y=1.3, color=1), Cone(x=1.4, y=1.9, color=1), Cone(x=1.9, y=3.1, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.3),
    ),

    # 32: right curve, only 3 yellow cones (inside of the turn), no blue
    "32": (
        [Cone(x=1.2, y=1.2, color=0), Cone(x=2.2, y=2.4, color=0), Cone(x=3.5, y=2.9, color=0)],
        CarPose(x=0.0, y=0.0, yaw=1.2),
    ),

    # 33: diagonal track, 3 blue cones with uneven spacing, no yellow
    "33": (
        [Cone(x=0.5, y=2.0, color=1), Cone(x=1.6, y=3.1, color=1), Cone(x=3.2, y=4.3, color=1)],
        CarPose(x=0.0, y=0.0, yaw=0.7),
    ),

    # 34: left curve, 3 yellow cones (outside of the turn) + 1 blue close to the car
    "34": (
        [Cone(x=0.3, y=1.6, color=1),
         Cone(x=1.7, y=0.2, color=0), Cone(x=2.8, y=1.4, color=0), Cone(x=3.5, y=3.0, color=0)],
        CarPose(x=0.0, y=0.0, yaw=0.85),
    ),

    # 35: tighter right turn, 3 blue cones (outside of the turn), no yellow
    "35": (
        [Cone(x=-0.7, y=1.3, color=1), Cone(x=0.0, y=2.6, color=1), Cone(x=1.3, y=3.9, color=1)],
        CarPose(x=0.0, y=0.0, yaw=1.3),
    ),
}


def get_scenario_names() -> List[str]:
    return sorted(_SCENARIOS.keys(), key=lambda s: int(s))


def make_scenario(name: str) -> Tuple[List[Cone], CarPose]:
    if name not in _SCENARIOS:
        valid = ", ".join(get_scenario_names())
        raise ValueError(f"Unknown scenario '{name}'. Valid options: {valid}")
    cones, car = _SCENARIOS[name]
    return list(cones), CarPose(x=car.x, y=car.y, yaw=car.yaw)
