---
beat: ten_thalos_emerges
act: 3
pov: freddy
location: Sea-cave entrance
time: Midnight, storm approaching
---

## Summary
Freddy follows Kai to the sea-cave and witnesses the confrontation. Thalos emerges from the deep—massive, ancient, terrifying. Kai transforms fully for the first time in front of Freddy. The choice: run, or stand with the monster you love.

## Key Events
- Freddy finds Kai at the cave entrance, tense and watching
- The water churns; something vast rises
- Thalos emerges: tentacles, red bioluminescence, voice like crushing waves
- "Little guardian. You've grown soft. Found a pet."
- Kai's transformation: spire-crest rises, arms split into sucker-limbs
- Freddy sees Kai's full monster form for the first time

## Axis Shifts
- threat: +4 (now at 9)
- sanctuary: -1 (now at 4)
- trust: -2 (strain under pressure)
- revelation: +3 (full reveal)

## Choices

### Choice A: "Stay. No matter what he looks like, he's still Kai."
- target: scene_ten_intimacy_and_threat
- type: CONTINUE
- shifts: trust +3
- note: Freddy's loyalty despite fear—critical romance moment

### Choice B: "Shout a distraction—draw Thalos's attention"
- target: scene_freddy_bait
- type: ALTERNATE
- shifts: threat +1, trust +2
- note: Brave but dangerous, Kai will have to protect him

### Choice C: "Run to get help from the town"
- target: scene_town_warning
- type: ALTERNATE
- shifts: belonging +2
- note: Freddy involves the community, slower resolution

### Choice D: "Freeze—you can't process what you're seeing"
- target: scene_ten_thalos_emerges
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "Your legs won't move. Kai glances back. 'Freddy. Go or stay. But choose.'"
  - attempt_2: "Thalos laughs, the sound like drowning. Kai steps between you and the predator. Choose."
  - attempt_3: "Kai's hand—human-shaped, trembling—reaches back toward you. You take it."

### Choice E: "[DEAD END] Run and don't look back"
- target: scene_freddy_abandons
- type: DEAD_END
- shifts: trust: -10, belonging: -5
- ending_text: "You run. You don't stop until you're in your car, then the highway. Starlight Cove shrinks in your mirror. You never learn what happened to Kai. Some nights, you swear you see a shimmer in tide-pools far from any coast. But you never stop to look."

## Mood
Terrifying, beautiful, the crucible moment

## Notes
- CRITICAL SCENE: Freddy's choice determines everything
- Dead end must feel earned, not punishing—consequences of fear
- Kai's monster form should be awe-inspiring, not repulsive
