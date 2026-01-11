---
beat: sho_moonlit_walk
act: 2
pov: freddy
location: Boardwalk, between diner and tide-pool
time: Midnight, full moon
---

## Summary
Freddy and Kai walk the boardwalk after closing. First real conversation. Kai speaks in fragments about "the old guardians" and his duty. Freddy notices the shimmer on Kai's arms intensifies in moonlight. They almost touch—fingers brushing—before Kai pulls away.

## Key Events
- Kai appears at Freddy's usual spot on the boardwalk
- First spoken words between them—Kai's voice like waves
- Kai mentions "the others are gone" and "I stayed to watch"
- Freddy sees the bioluminescent shimmer clearly—not a trick
- Their hands almost touch; Kai withdraws, conflicted
- Freddy asks "Will you be here tomorrow?" Kai nods.

## Axis Shifts
- intimacy: +5
- trust: +2
- revelation: +2

## Choices

### Choice A: "Ask about the shimmer on his arms"
- target: scene_sho_sea_cave
- type: CONTINUE
- shifts: revelation +2
- note: Freddy pushes for truth, Kai respects it

### Choice B: "Let the silence speak—walk beside him without questions"
- target: scene_sho_sea_cave
- type: ALTERNATE
- shifts: intimacy +1, trust +1
- note: Patience rewarded, same destination

### Choice C: "Reach for his hand"
- target: scene_almost_touch
- type: CONTINUE
- shifts: intimacy +2
- note: Bold move, Kai will pull away but remember

### Choice D: "Tell him about your own past—the city, the breakdown"
- target: scene_freddy_opens
- type: ALTERNATE
- shifts: trust +2, belonging +1
- note: Vulnerability begets vulnerability

### Choice E: "Make an excuse to leave—this is too fast"
- target: scene_sho_moonlit_walk
- type: LOOP
- max_attempts: 3
- escalation:
  - attempt_1: "You stammer something about early morning. He nods, but his eyes hold yours. You don't move."
  - attempt_2: "You turn to go. Two steps. Three. The tide-pool pulses behind you. You stop."
  - attempt_3: "Your feet won't carry you away. 'Tomorrow,' he says softly. You nod."

## Mood
Tender, charged, moonlit liminal space

## Notes
- CRITICAL romance beat: first real connection
- Kai's dialogue should be sparse, wave-like rhythms
- The almost-touch must feel electric, not awkward
