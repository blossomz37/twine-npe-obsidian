---
beat: ki_kai_routine
act: 1
pov: kai
location: Tide-pool sanctuary
time: Deep night, moon at zenith
---

## Summary
Kai performs his nightly ritual at the tide-pool, checking the Lunar Shell artifact's glow. He senses Freddy's presence nearby—a human watching, not fleeing. For the first time in years, someone stays.

## Key Events
- Kai kneels at tide-pool edge, hand in glowing water
- The Lunar Shell pulses beneath the surface, stable
- Kai senses Freddy's heartbeat from the boardwalk—human, curious, unafraid
- He allows Freddy to watch, doesn't chase him away
- A silent acknowledgment: Kai inclines his head toward Freddy before diving

## Axis Shifts
- sanctuary: 10 (stable, confirmed)
- revelation: +1

## Choices

### Choice A: "Let the human watch—just this once"
- target: scene_sho_quiet_night
- type: CONTINUE
- shifts: trust +1
- note: Kai makes first gesture of acceptance

### Choice B: "Vanish into the sea before he gets closer"
- target: scene_kai_avoidance
- type: ALTERNATE
- shifts: sanctuary +0, trust -1
- note: Delays connection, adds scene of Kai's internal conflict

### Choice C: "Surface and confront him—warn him away"
- target: scene_ki_kai_routine
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You rise, ready to snarl. But his eyes—they're not afraid. You sink back."
  - attempt_2: "You prepare the words: leave, danger, not for you. But he's still there, patient. The words dissolve."
  - attempt_3: "You surface. He doesn't flinch. And you realize—you don't want him to leave."

### Choice D: "[IF revelation >= 3] Show him your true form"
- target: scene_first_reveal
- type: GATE
- requires: revelation >= 3
- shifts: revelation +2, trust +2
- unlock_text: "Something in his steady gaze makes you wonder: what if he saw you? Really saw you?"

## Mood
Sacred, vigilant, a crack in solitude

## Notes
- Establish Kai's guardian duty and the artifact's importance
- First POV from Kai—different voice, water-imagery
- The gated choice rewards players who've built revelation
