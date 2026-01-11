---
beat: sho_sea_cave
act: 2
pov: freddy
location: Sea-cave stairway
time: Early morning, before dawn
---

## Summary
Kai leads Freddy down the hidden sea-cave stairway. Freddy sees the deeper world beneath Starlight Cove—bioluminescent walls, the echo of ancient tides, the edge of something sacred. Kai stops before the inner grotto: "Not yet. But soon."

## Key Events
- Kai invites Freddy to follow ("There's something I want you to see")
- Hidden stairway behind the rock outcrop, worn by centuries
- Sea-cave walls glow with life—Freddy's first glimpse of Kai's world
- The deeper grotto entrance: Kai pauses, conflicted
- "This is where I live. Where I guard. But you're not ready—and neither am I."
- They ascend together; Freddy doesn't push

## Axis Shifts
- revelation: +1 (more to come)
- intimacy: +2
- belonging: +3

## Choices

### Choice A: "Accept his pace—you'll wait until he's ready"
- target: scene_ten_fade_wave
- type: CONTINUE
- shifts: trust +2
- note: Main path forward, respects Kai's boundaries

### Choice B: "Ask what he's guarding—press gently"
- target: scene_artifact_hint
- type: ALTERNATE
- shifts: revelation +2
- note: Kai reveals more about the Lunar Shell, still doesn't show it

### Choice C: "Take his hand as you climb the stairs"
- target: scene_stair_intimacy
- type: ALTERNATE
- shifts: intimacy +2
- note: Physical connection beats verbal

### Choice D: "Try to go deeper without permission"
- target: scene_sho_sea_cave
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You take a step past him. He doesn't stop you—but his shoulders tense. You hesitate."
  - attempt_2: "Another step. The cave grows colder. Kai's eyes flash with something old. 'Please,' he says."
  - attempt_3: "You stop. Whatever's down there, it's not yours to take. 'I'll wait,' you say. He exhales."

### Choice E: "[IF revelation >= 5] 'Show me what you really are'"
- target: scene_full_form_reveal
- type: GATE
- requires: revelation >= 5
- shifts: revelation +3, intimacy +2
- unlock_text: "You've seen enough fragments. It's time for the whole truth."

## Mood
Sacred, hushed, the threshold of transformation

## Notes
- End of Shō—relationship is built, revelation close but not complete
- The grotto is the heart of Kai's world; saving it for later is important
- Freddy's patience here earns Kai's trust for Ten act
