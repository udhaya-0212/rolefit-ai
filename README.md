# RoleFit AI

RoleFit compares a resume with a target job description. It retrieves the closest resume evidence for each requirement and reports transparent weighted evidence coverage. This is a self-coaching prototype, not an ATS or hiring decision system.

## Live app

https://rolefit-ai.netlify.app

## Run locally

1. Install Python 3.
2. Double-click `Start-RoleFit.bat` on Windows, or run `python rolefit_server.py`.
3. Open `http://127.0.0.1:8765/rolefit-ai.html`.
4. Paste text, browse for a resume, or drag a supported file into the app. The first OCR or AI run needs internet to load browser libraries and model assets.

The local server binds to `127.0.0.1` only.

## Supported files

- Text: `.txt`, `.md`, `.csv`
- Word: `.docx`
- PDF: selectable text and scanned/image PDF (OCR handles up to the first 8 scanned pages)
- Images: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`

The app checks file signatures as well as extensions. Review OCR output because names, symbols, and technical terms can be misread. Save older `.doc` documents as `.docx` first.

## AI, scoring, and privacy

Transformers.js runs `Xenova/all-MiniLM-L6-v2` in the browser to create sentence embeddings. It shows the closest resume evidence and semantic similarity for each job requirement. Phrase overlap also affects evidence retrieval. The weighted score gives 1 to strong text matches, 0.5 to related wording, and 0 to no clear wording match; explicit must/required/minimum/essential requirements receive extra weight.

Similarity is not probability, and the score is not accuracy or interview likelihood. The thresholds are demo values. The model is general-purpose English and has no labelled benchmark or fairness evaluation. Inspect the evidence and only claim experience that is true.

Resume and job text are processed in the browser; they are not sent to an AI API or stored by the local server. The app downloads public JS libraries and model/OCR assets from CDNs, so first use requires internet.

## Project files

- `index.html` — hosted entry point.
- `rolefit-ai.html` — main app page.
- `netlify.toml` — static publish configuration and response headers.
- `rolefit_server.py` and `Start-RoleFit.bat` — local launcher.
- `rolefit-ai-project-guide.md` — architecture, placement explanation, and limitations.
- `rolefit-sample-resume.txt` and `rolefit-sample-job-description.txt` — fictional demo data.

## Deployment

The public source is at https://github.com/udhaya-0212/rolefit-ai. Netlify is connected to the `main` branch and automatically publishes new commits. No build command is needed; Netlify serves `index.html`. Production is public, while deploy previews are private.

Keep personal resumes and contact details out of this public repository.
