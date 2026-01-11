---
beat: ki_freddy_arrives
act: 1
pov: freddy
location: Starlight Cove Diner
time: Late night, first shift
---

## Summary
Freddy Gray arrives at the Starlight Cove Diner for his first late-night shift. Through the window, he catches his first glimpse of the mysterious tide-pool. The café cook welcomes him, and Freddy begins to settle into his new life.

## Key Events
- Freddy enters the diner, noting the salt-heavy air and worn counter
- Café cook (spiky blond hair, wave tattoo) greets him warmly
- Through the window: tide-pool glows faintly under the moon
- A figure on the distant rock outcrop, barely visible

## Axis Shifts
- belonging: +1

## Choices

### Choice A: "Step outside to look at the tide-pool"
- target: scene_ki_first_sighting
- type: CONTINUE
- shifts: revelation +1
- note: Leads directly to first Kai sighting

### Choice B: "Focus on learning the diner routine"
- target: scene_diner_settling
- type: ALTERNATE
- shifts: belonging +1
- note: Slower path, builds community first, still reaches first sighting later

### Choice C: "This was a mistake—call someone back home"
- target: scene_ki_freddy_arrives
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "The phone rings twice before you hang up. What would you even say? You're here now. The cook glances over with understanding eyes."
  - attempt_2: "Your thumb hovers over the call button. The cook slides a cup of coffee toward you. 'First nights are the hardest,' he says. 'Give it a chance.'"
  - attempt_3: "You pocket the phone. There's nothing back there for you anymore. The tide-pool catches the moonlight, almost beckoning."
- shifts: belonging -1 (per attempt)

## Mood
Quiet anticipation, gentle melancholy, fresh start energy

## Notes
- Establish Freddy's outsider status
- Hint at the mysterious tide-pool without revealing too much
- Cook serves as warm welcome to the community
