---
beat: ten_fade_wave
act: 3
pov: kai
location: Tide-pool sanctuary
time: Deep night, new moon
---

## Summary
Kai senses something wrong. The tide-pool's glow flickers and dims—the Lunar Shell is weakening. He finds strange tracks on the rocks: too large, too many limbs. Thalos is near. Kai must decide whether to face this alone or trust Freddy with the truth.

## Key Events
- Kai's nightly ritual; the glow is weaker than before
- He touches the water—the Shell's pulse is erratic, frightened
- Strange marks on the outcrop: sucker-prints, claw-gouges
- Kai recognizes them—Thalos's signature
- The sanctuary is no longer safe; the predator has returned
- Kai sees the diner's light—Freddy is still there

## Axis Shifts
- sanctuary: -5 (drops to 5)
- threat: +5

## Choices

### Choice A: "Go to Freddy—tell him everything"
- target: scene_ten_thalos_emerges
- type: CONTINUE
- shifts: trust +2, revelation +2
- note: Kai chooses partnership over solitude

### Choice B: "Hunt Thalos alone—protect Freddy by keeping him ignorant"
- target: scene_kai_hunts_alone
- type: ALTERNATE
- shifts: threat +1, trust -2
- note: Sets up rescue scenario, Kai gets hurt

### Choice C: "Strengthen the wards first—delay the confrontation"
- target: scene_ten_fade_wave
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You press power into the wards. They flicker brighter, then fade. The Shell is too weak."
  - attempt_2: "You try again. The tide-pool dims further. Whatever is coming, it's not stopping for wards."
  - attempt_3: "The glow gutters out completely. In the darkness, you hear it: waves breaking wrong. He's here."

### Choice D: "[IF trust >= 8] Let Freddy find you—he'll come"
- target: scene_freddy_finds_kai
- type: GATE
- requires: trust >= 8
- shifts: trust +2, intimacy +1
- unlock_text: "You don't have to go to him. He knows. He's already walking toward the tide-pool."

## Mood
Dread-tinged, ominous stillness before storm

## Notes
- This is the TURN—tone shifts from cozy to urgent
- Kai's isolation impulse vs. new trust in Freddy
- Sanctuary axis drops significantly—stakes are real now
