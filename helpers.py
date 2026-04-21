from typing import List, Dict


def average_fps(fps_list: List[float]) -> float:
    """Calculate the average frames per second (FPS) from a list of FPS values.

    Args:
        fps_list (List[float]): A list of FPS values.

    Returns:
        float: The average FPS.
    """
    return sum(fps_list) / len(fps_list) if fps_list else 0.0


def filter_high_fps(fps_data: Dict[str, List[float]], threshold: float) -> Dict[str, List[float]]:
    """Filter FPS data by a defined threshold.

    Args:
        fps_data (Dict[str, List[float]]): A dictionary of game names and their corresponding FPS values.
        threshold (float): The minimum FPS value to keep.

    Returns:
        Dict[str, List[float]]: Filtered dictionary with games meeting the FPS threshold.
    """
    return {game: [fps for fps in fps_values if fps >= threshold] 
            for game, fps_values in fps_data.items()}


def format_fps_stats(fps_data: Dict[str, List[float]]) -> str:
    """Generate a formatted string of FPS statistics.

    Args:
        fps_data (Dict[str, List[float]]): A dictionary with game names and FPS values.

    Returns:
        str: A formatted string representation of the FPS statistics.
    """
    stats = [f'{game}: Avg FPS = {average_fps(fps_values):.2f}' 
             for game, fps_values in fps_data.items()]
    return '\n'.join(stats)
