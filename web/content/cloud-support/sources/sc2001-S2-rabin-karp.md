# How do rolling hashes make Rabin–Karp work?

## Sources

String Matching pp11–15,20–24; study notes 07-string-matching §§7.3–7.4.

Recording: unavailable for this material. User approved slides-and-notes grounding on 24 October 2026.

Physical PDF pages are used. Fresh examples and explicit derivations are explanatory additions, not recording quotations.

## Narration

### b00 — Reuse the window hash

How do rolling hashes make Rabin–Karp work? We will encode a window, derive its constant-work rolling update, and follow a collision all the way through actual character verification.

### b01 — Positional encoding

Map alphabet characters to integer codes and interpret a window of m characters as a base-d number. The leftmost code multiplies d to the m minus one, with successive codes using decreasing powers.

### b02 — Horner evaluation

Horner evaluation builds this number by multiplying the current value by d and adding the next code. This requires one pass through m symbols instead of separately computing a power for every term.

### b03 — Derive a rolling update

For decimal window three six four one five followed by an incoming two, remove the leading three times ten thousand. Multiply the remainder by ten and append two, obtaining six four one five two.

### b04 — The rolling formula

The general update subtracts the outgoing code times d to the m minus one, then multiplies by d and adds the incoming code. Precompute that leading place value, since it is the same at every alignment.

### b05 — Use modular hashes

Exact encodings become enormous for long patterns, so Rabin–Karp keeps their residues modulo a chosen prime q. Compute both initial hashes with modular Horner evaluation and precompute H modulo q.

### b06 — An intentional collision

Now take decimal pattern twenty-five, text one two two five, base ten and modulus thirteen. The pattern hash is twelve, and the first text window twelve also hashes to twelve, even though the strings differ.

### b07 — Verify the candidate

Equal hashes therefore request a character check rather than proving success. Comparing the first digits rejects window twelve immediately, because pattern two differs from text one.

### b08 — Roll and find the match

Roll to window twenty-two, whose hash is nine, so its different hash rejects it without character verification. Roll once more to window twenty-five, whose hash is twelve and whose two characters both match, giving zero-based index two.

### b09 — Check the arithmetic

With H equal to ten, the first modular roll is twelve minus one times ten, multiplied by ten, plus two, all modulo thirteen. The result is twenty-two modulo thirteen, or nine; the next roll must normalise its negative intermediate residue if the language uses signed remainders.

### b10 — The basic cost components

Initial hashing costs big O of m, and each rolling update uses constant word arithmetic. Verification adds work whenever hashes agree, so a full runtime statement must count those candidate checks rather than declaring every scan unconditionally linear.

### b11 — Things to take note of

Things to take note of: use the same encoding and modulus for both hashes, precompute the leading place value, and verify every equal-hash candidate. Roll only when another complete window exists, preserve modulo conventions, and remember that a collision is expected behaviour for a hash, not permission to return the wrong answer.
