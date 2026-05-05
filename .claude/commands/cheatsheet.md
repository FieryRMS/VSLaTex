# Cheatsheet Writing Guide

## Language
- Terse: drop articles and filler ("Delay O(n)", not "The delay is O(n)")
- Use symbols over words: `$\to$`, `$\Rightarrow$`, `$\uparrow$`, `$\downarrow$`
- Bold key terms on first use: `\textbf{term}`

## Structure
- One `\section{}` per topic, each containing a single `\itemize`
- Nested `\itemize` for sub-points (max 2 levels)
- Worked examples: `\textbf{Ex}` bullet with step-by-step sub-bullets
- Tables: plain `tabular`, narrow columns, no decorative lines. for long content, use simple itemize instead of tables.

## Math
- All symbols/formulas in inline math `$...$`
- Suppress spacing in compressed expressions: `{=}`, `{+}`, `{-}`
- No display math (`$$` or `equation`) — wastes vertical space

## What to avoid/Restrictions
- No prose paragraphs
- No redundant labels ("Note:", "Remember:")
- No multi-line display math
- Never use any unicode characters (e.g., arrows, bullets) - stick to LaTeX commands only
- avoid using \texttt{} or \verb|| or similar non-breaking formats for long expressions, as it will overflow