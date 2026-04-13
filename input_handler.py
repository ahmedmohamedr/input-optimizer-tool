import json
from typing import Any, Dict, List


def load_keybindings(file_path: str) -> Dict[str, str]:
    """
    Load key bindings from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing key bindings.

    Returns:
        Dict[str, str]: A dictionary mapping action names to key bindings.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contents cannot be parsed as JSON.
    """
    with open(file_path, 'r') as file:
        keybindings = json.load(file)
    return keybindings


def save_keybindings(file_path: str, keybindings: Dict[str, str]) -> None:
    """
    Save key bindings to a JSON file.

    Args:
        file_path (str): The path to the JSON file where key bindings will be saved.
        keybindings (Dict[str, str]): A dictionary mapping action names to key bindings.

    Raises:
        IOError: If the file cannot be opened for writing.
    """
    with open(file_path, 'w') as file:
        json.dump(keybindings, file, indent=4)


def get_keybinding(action: str, keybindings: Dict[str, str]) -> str:
    """
    Retrieve the key binding for a given action.

    Args:
        action (str): The action for which to retrieve the key binding.
        keybindings (Dict[str, str]): A dictionary mapping action names to key bindings.

    Returns:
        str: The key binding for the specified action.

    Raises:
        KeyError: If the action does not have an assigned key binding.
    """
    return keybindings[action]


def list_actions(keybindings: Dict[str, str]) -> List[str]:
    """
    List all actions that have key bindings assigned.

    Args:
        keybindings (Dict[str, str]): A dictionary mapping action names to key bindings.

    Returns:
        List[str]: A list of action names.
    """
    return list(keybindings.keys())
