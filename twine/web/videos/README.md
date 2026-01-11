# Scene Videos

This folder contains 8-second video loops for each scene in the Twine story.

## Expected Files

| Video File     | Scene                  | Description                            |
| -------------- | ---------------------- | -------------------------------------- |
| `scene_1.mp4`  | Ki: Freddy Arrives     | Diner window, tide-pool glowing beyond |
| `scene_2.mp4`  | Ki: First Sighting     | Kai on rocks, moonlit shimmer          |
| `scene_3.mp4`  | Ki: Kai Routine        | Kai at tide-pool, guardian ritual      |
| `scene_4.mp4`  | Shō: Quiet Night       | Objects moving, coffee offering        |
| `scene_5.mp4`  | Shō: Moonlit Walk      | Two figures, hands almost touching     |
| `scene_6.mp4`  | Shō: Sea Cave          | Bioluminescent stairway descent        |
| `scene_7.mp4`  | Ten: Fade Wave         | Flickering tide-pool, claw marks       |
| `scene_8.mp4`  | Ten: Thalos Emerges    | Monster rising, Kai transforms         |
| `scene_9.mp4`  | Ten: Intimacy & Threat | Grotto embrace, Shell pulsing          |
| `scene_10.mp4` | Ketsu: Stand Together  | Battle scene, "I fight for home"       |
| `scene_11.mp4` | Ketsu: Defeated        | Shell blazing, Kai collapses           |
| `scene_12.mp4` | Ketsu: Community       | Festival, acceptance                   |
| `scene_13.mp4` | Epilogue               | Restored grotto, HEA                   |

## How It Works

1. **Add videos** to this folder following the naming convention above
2. **Enable videos** in `StoryInit` by setting the scene to `true`:
   ```
   <<set $sceneVideos["scene_1"] to true>>
   ```
3. **Use in passages** with the widget:
   ```
   <<scenevideo "scene_1">>
   ```

## Video Specifications

- **Duration:** 8 seconds (looping)
- **Format:** MP4 (H.264)
- **Resolution:** 1920x1080 or 1280x720
- **Aspect Ratio:** 16:9
- **Audio:** Muted by default (can add ambient sound separately)

## Generating Videos

Use the prompts from `scene_list.md` with:
- Runway Gen-3
- Pika Labs  
- Kling AI
- Luma Dream Machine

## Fallback Behavior

If a video doesn't exist (scene set to `false`), the widget outputs nothing—the passage displays normally without video.
