---
beat: ki_first_sighting
act: 1
pov: freddy
location: Boardwalk rock outcrop
time: Late night, after closing
---

## Summary
Freddy steps outside after his shift and sees a figure standing motionless on the rock outcrop. The moonlight catches something strange—a shimmer along the stranger's arms. Their eyes meet briefly before the figure disappears toward the tide-pool.

## Key Events
- Freddy finishes closing up, drawn outside by the glow
- A tall figure (Kai) stands on the outcrop, barefoot, watching the water
- Moonlight reveals teal shimmer on Kai's arms—wrong for human
- Their eyes meet; Kai holds Freddy's gaze, then turns away
- Kai vanishes toward the tide-pool with inhuman grace

## Axis Shifts
- revelation: +2
- trust: +1

## Choices

### Choice A: "Follow him to the tide-pool"
- target: scene_ki_kai_routine
- type: CONTINUE
- shifts: revelation +1, trust +1
- note: Direct path, accelerates connection

### Choice B: "Watch from the boardwalk, let him go"
- target: scene_ki_kai_routine_distant
- type: ALTERNATE
- shifts: trust +1
- note: Slower, Kai notices Freddy's respectful distance later

### Choice C: "Convince yourself it was nothing—go home"
- target: scene_ki_first_sighting
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You shake your head. Trick of the light. You walk toward your car, but glance back—he's still there, waiting."
  - attempt_2: "Just exhaustion. First week nerves. You turn away, but your feet don't move. The shimmer pulses once, like a heartbeat."
  - attempt_3: "Your keys are in your hand. But the tide-pool glows brighter, and you realize: you didn't come here to look away."

## Mood
Liminal, mysterious, electric stillness

## Notes
- First visual confirmation of Kai's inhuman nature
- Freddy's curiosity should feel inevitable, not reckless
- Kai should feel watchful but non-threatening
