# RoleFit AI — Project & Placement Guide

## What it does

RoleFit compares a resume to a particular job description. It extracts requirement sentences, compares each against resume sentences with a sentence-embedding model, and presents the closest resume evidence beside a match label. The user can inspect the wording and decide whether it truthfully demonstrates the requirement.

## What is included

- Responsive career dashboard with animated evidence coverage.
- Paste text with Ctrl+V, browse or drag and drop a `.txt`, `.md`, `.csv`, selectable-text `.pdf`, `.docx`, `.jpg/.jpeg`, `.png`, `.webp`, or `.bmp` resume.
- Extract PDF text with PDF.js, DOCX text with Mammoth, and image/scanned PDF text with Tesseract.js OCR. The picker intentionally has no restrictive extension filter, and checks file signatures so an image with a `.pdf` name is recognized correctly.
- Extract up to 14 requirement statements from job text and compare against up to 70 resume sentences.
- In-browser semantic embeddings using `Xenova/all-MiniLM-L6-v2` through Transformers.js.
- Best resume evidence sentence shown for every requirement, with strong/related/unmatched statuses.
- Transparent score and scoring/limitations explainer.
- A clearly labelled keyword fallback if the model cannot load. The UI must not claim that fallback is AI.
- Local-only HTTP launcher, avoiding `file://` restrictions that interfere with clipboard, modules and browser security.

## How to run it

1. Install Python 3 if it is not already available.
2. Double-click `Start-RoleFit.bat` in the outputs folder.
3. Keep the console window open; it starts a loopback-only server and opens RoleFit in your browser. Press Ctrl+C in the console to stop it.
4. The first semantic analysis needs internet to download the JavaScript runtime and model weights. They are cached by the browser. Later runs should load from cache.
5. Paste both documents or upload/drag a supported resume. Wait for the AI status, then click **Analyze match**. A detailed evidence list appears below.

The server binds only to `127.0.0.1`, so it is available only on this computer. Resume and job text are processed in the browser; neither is sent to an AI API. The model and PDF/DOCX parser libraries are downloaded from public CDNs. PDF.js is used for selectable text PDFs; scanned documents need OCR which is not part of this version.

## What the score means

The score is **weighted evidence coverage**, not model accuracy and not probability of getting an interview. Each requirement receives 1 point for a strong text match, 0.5 for related wording, and 0 for no clear wording match. Requirements containing explicit priority language (`must`, `required`, `minimum`, `essential`) receive extra weight. The model's cosine similarity and wording overlap appear beside every requirement to help the user inspect the decision. Similarity percentages are not confidence probabilities; even a strong text match may be driven by direct required terms.

Similarity thresholds are initial demo thresholds, not calibrated cutoffs. `all-MiniLM-L6-v2` is a general English sentence-embedding model; it is not trained to predict hiring decisions or evaluate candidate quality. It can miss evidence, infer a topical relation that is not proof of skill, and be affected by resume wording. The result requires human review.

Do not call the percentage “94% accurate.” Accuracy requires a labelled evaluation set with known matches/non-matches and measured precision, recall, and error analysis across roles and candidate groups. This project has no such validated dataset yet. A local browser smoke check exercised OCR and semantic matching. Its output is a weighted evidence-coverage estimate, not a measure of matching accuracy. 

## Tools used, and why

| Tool | Use |
| --- | --- |
| HTML/CSS | Structure and responsive visual dashboard. |
| JavaScript | Requirement extraction, evidence display, weights, text import and report UI. |
| Transformers.js 4.3.0 | Runs model inference in the browser without sending resume text to an AI service. |
| `Xenova/all-MiniLM-L6-v2` | Generates sentence embeddings so semantically similar wording can be compared, beyond exact keyword matching. |
| PDF.js and Mammoth | Extract selectable PDF and DOCX text in the browser. |
| Tesseract.js 6.0.1 | OCR for image resumes and scanned PDFs in the browser. |
| Python standard library | Serves the static page from `127.0.0.1`, enabling browser modules and native paste behavior without third-party Python packages. |

Transformers.js model pipeline usage and browser caching are described in the [official pipeline docs](https://github.com/huggingface/transformers.js/blob/main/packages/transformers/docs/source/pipelines.md); model embedding usage is in the [model card](https://huggingface.co/Xenova/all-MiniLM-L6-v2).

## Placement-class demo script (about 90 seconds)

> “I built RoleFit AI to help students tailor their resume to one target role. It extracts requirements from a job description, compares each requirement with resume sentences using a sentence-embedding model running in the browser, and shows the closest evidence sentence so the user can verify it. The score is weighted evidence coverage, not hiring probability. Resume content stays local. The current model is a general-purpose English model and the thresholds are a prototype; to claim accuracy, I would need a manually labelled, diverse evaluation set and precision/recall analysis. The next step is to evaluate it across different roles, then improve requirement extraction and document OCR based on measured errors.”

## Resume bullets — use only if you can explain them

- Built a browser-based resume-to-job matching prototype using Transformers.js and sentence embeddings, with requirement-level evidence snippets and a transparent weighted coverage score.
- Implemented local PDF/DOCX/text extraction, paste and drag/drop flows, and a loopback-only Python launcher; resume text is processed client-side and is not sent to a model API.
- Added explicit fallback and limitation messaging, distinguishing semantic AI output from keyword-only analysis and avoiding claims of hiring prediction or unvalidated accuracy.

## Limitations and next steps

This is a placement-ready prototype, not an industrial hiring product. It does not have a labelled benchmark, fairness audit, role-specific evaluation, OCR for scanned PDFs, persistent user accounts, database or hosted service. The model and OCR/PDF/DOCX libraries require internet on first load, then the browser can cache them. A local browser verification confirmed upload, OCR text review, model inference, evidence display, and a completed score. The current reference preview is local-only; no public deployment has been created yet. The fallback is rule-based and should be identified as such.

For production readiness: assemble a consented and anonymized benchmark; have people label requirement/evidence pairs; measure precision, recall and false-match rates across roles and candidate groups; tune thresholds using held-out data; add OCR only with user confirmation; and have qualified reviewers assess privacy, bias and accessibility. Do not use it to automatically reject applicants.
