# CriticMarkup Sample

This sample demonstrates **CriticMarkup** — supported by Pandoc for conversion to DOCX.

---

# Part 1: CriticMarkup

CriticMarkup is a syntax for editorial markup. Pandoc can process these with the right settings.

## Additions

{++This text was added.++}

Example in context:
The quick brown fox {++quickly++} jumps over the lazy dog.

## Deletions

{--This text was deleted.--}

Example in context:
The quick {--slow--} brown fox jumps over the lazy dog.

## Substitutions

{~~old text~>new text~~}

Example in context:
She walked {~~slowly~>quickly~~} through the garden.

## Comments

{>>COMMENT:This is a comment from the editor.<<}

Example in context:
The protagonist entered the room.{>>COPY EDIT:Consider adding more sensory details here.<<}

## Highlights

{==This text is highlighted for attention.==}

Example in context:
The key clue was hidden in {==the third paragraph of the letter==}.

---

# Part 2: Combined Example — Editing a Manuscript

Here's how an editor might use CriticMarkup on a manuscript:

---

## Chapter 1: The Arrival

{--It was a dark and stormy night.--}{++Lightning split the sky as rain hammered the windows.++}{>>COPY EDIT:Replaced cliché opening with more vivid imagery.<<}

Sarah {~~walked~>strode~~} into the manor, her coat dripping onto the marble floor. {==The butler was nowhere to be seen.==}{>>CLUE:This becomes important in Chapter 5.<<}

"Hello?" she called out. {++Her voice echoed through the empty halls.++}

{--She felt scared.--}{++She tightened her grip on the blanket as shadows danced in the flickering candlelight.++}{>>COPY EDIT:Show, don't tell.<<}

---

# Conversion Notes

To convert this file with proper CriticMarkup formatting, use:

```bash
python convert_with_critic.py
```

This applies color-coded formatting:
- **Additions** → Green text, underlined
- **Deletions** → Red text, strikethrough  
- **Substitutions** → Red strikethrough → Green underline
- **Comments** → Yellow highlight, gray italic
- **Highlights** → Yellow background

---

*This sample demonstrates CriticMarkup for editorial annotations.*
<!--This is a hiddent text comment>