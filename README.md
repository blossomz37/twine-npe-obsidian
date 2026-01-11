# 🌊 Midnight at Starlight Cove

An interactive monster romance visual novel built with Twine and the Narrative Physics Engine (NPE).

**[▶️ Play Now](https://blossomz37.github.io/twine-npe-obsidian/)**

---

## About

Freddy arrives in the sleepy coastal town of Starlight Cove for a fresh start—and discovers that the mysterious figure haunting the tide-pool is far more than human. As feelings deepen, an ancient threat emerges from the deep.

### Features

- 🎭 **55 illustrated passages** with AI-generated artwork
- 🎬 **13 looping video scenes** for key story moments
- 🔄 **Multiple endings** based on your choices
- 📊 **NPE tension tracking** (belonging, trust, revelation, intimacy, threat, sanctuary)
- 🔁 **Loop mechanics** that evolve with repeated choices

---

## Story Structure

The narrative follows **Kishōtenketsu** (起承転結) structure:

| Act   | Japanese | Meaning      | Content                                 |
| ----- | -------- | ------------ | --------------------------------------- |
| Ki    | 起       | Introduction | Freddy arrives, first sighting of Kai   |
| Shō   | 承       | Development  | Building trust, moonlit walks, sea cave |
| Ten   | 転       | Twist        | Thalos emerges, the Shell is threatened |
| Ketsu | 結       | Resolution   | Final confrontation, multiple endings   |

---

## Project Structure

```
├── docs/                    # GitHub Pages deployment
│   ├── index.html          # Compiled Twine game
│   ├── images/             # 55 passage illustrations
│   └── videos/             # 13 scene videos
├── twine/
│   ├── midnight_starlight_v3.twee   # Source file with widgets
│   ├── npe_config.yaml              # NPE configuration
│   └── scenes/                      # Scene card documentation
├── character-sheets-images/         # Character reference art
└── story-bible/                     # Story documentation
```

---

## Technical Details

### Built With

- **[Twine](https://twinery.org/)** - Interactive fiction engine
- **[SugarCube 2.37](https://www.motoslave.net/sugarcube/2/)** - Story format
- **Narrative Physics Engine (NPE)** - Tension axis system

### Custom Widgets

```
<<scenevideo "scene_1">>     # Inserts looping video
<<passageimage "01_start">>  # Inserts passage illustration
```

### NPE Tension Axes

| Axis       | Range | Tracks                               |
| ---------- | ----- | ------------------------------------ |
| Belonging  | 0-15  | Freddy's connection to the town      |
| Trust      | 0-15  | Mutual trust between Freddy and Kai  |
| Revelation | 0-10  | How much of Kai's nature is revealed |
| Intimacy   | 0-15  | Emotional/physical closeness         |
| Threat     | 0-12  | Danger level from Thalos             |
| Sanctuary  | 0-10  | Safety of the tide-pool sanctuary    |

---

## Development

### Editing the Story

1. Import `twine/midnight_starlight_v3.twee` into Twine
2. Make your changes
3. Publish to File → save to `docs/index.html`
4. Run path conversion if using local absolute paths

### Local Testing

Open `docs/index.html` directly in a browser. Videos and images use relative paths.

---

## Credits

- **Story & Design**: Carlo (blossomz37)
- **Built with**: Twine, SugarCube, NPE
- **Artwork**: AI-generated with character consistency
- **Videos**: AI-generated scene loops

---

## License

This project is for personal/educational use. Story content © 2025.
