# Twee Development

This directory contains the source code for "Midnight At Starlight Cove".

## Working with Components

To improve maintainability, the monolithic Twee file has been split into components in the `draft_components` directory.

### Directory Structure

- `draft_components/`: Contains the extracted components.
  - `StoryTitle.twee`: The story title.
  - `StoryData.twee`: Configuration and metadata.
  - `StoryInit.twee`: Initialization variables.
  - `StoryStylesheet.twee`: CSS styles.
  - `StoryScript.twee`: JavaScript code.
  - `StoryCaption.twee`: Sidebar caption.
  - `Widgets.twee`: Custom widgets (PassageImage, SceneVideo).
  - `story_passages.twee`: The main story content, sorted by passage image ID.
- `tools/`: Python scripts for management.
  - `extract_twee_components.py`: Extracts and sorts components from a monolithic file.
  - `compile_twee.py`: Compiles components into a single Twee file for testing/import.

### Workflow

1.  **Edit**: modifying the individual components in `draft_components/`.
2.  **Compile**: Run `python3 tools/compile_twee.py` to generate `midnight_working_copy_v2.twee`.
3.  **Test**: Import the compiled file into Twine or build with Tweego.

## References

- [SugarCube 2 Documentation](https://www.motoslave.net/sugarcube/2/docs/): Technical reference for the story format.
