---
beat: sho_quiet_night
act: 2
pov: freddy
location: Starlight Cove Diner
time: Late night, slow shift
---

## Summary
A quiet night at the diner. Freddy works alone, but strange things keep happening—a door closes on its own, a mug appears where he needed it, salt refills itself. Kai is helping, unseen. By shift's end, Freddy leaves a thank-you coffee on the back step.

## Key Events
- Empty diner, Freddy restocking and cleaning
- Door to cold storage swings shut by itself—saves his fingers
- A mug slides six inches toward him when he reaches
- Freddy realizes he's being watched, helped—not threatened
- He brews a coffee and leaves it on the back step, facing the tide-pool

## Axis Shifts
- trust: +3
- belonging: +1

## Choices

### Choice A: "Leave the coffee and say 'thank you' aloud"
- target: scene_sho_moonlit_walk
- type: CONTINUE
- shifts: trust +1
- note: Direct acknowledgment, Kai will respond next scene

### Choice B: "Leave the coffee, but don't say anything—let him come to you"
- target: scene_sho_moonlit_walk
- type: ALTERNATE
- shifts: belonging +1
- note: More patient approach, same destination

### Choice C: "Pretend you didn't notice—you're not ready for this"
- target: scene_sho_quiet_night
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You wipe down the counter again. The salt shaker slides another inch. He's patient."
  - attempt_2: "You check the locks twice. When you turn, the coffee pot is already on. He's still here."
  - attempt_3: "You stand at the back door. The tide-pool glows. Okay. Fine. You set down the coffee."

### Choice D: "[IF trust < 2] Call the café cook to stay late with you"
- target: scene_cook_night
- type: GATE
- requires: trust < 2
- shifts: belonging +1
- unlock_text: "Something's watching. You're not ready to face it alone."
- note: Safety branch for low-trust players

## Mood
Cozy eeriness, domestic intimacy with the unknown

## Notes
- First scene of Kai actively helping (not just watching)
- Build trust through small domestic miracles
- The coffee offering is a ritual start
