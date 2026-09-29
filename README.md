# RoleFit AI

RoleFit compares a resume with a target job description. It uses a sentence-embedding model to retrieve the closest resume evidence for each job requirement and calculates a transparent evidence-coverage score. It is a self-coaching prototype, not a hiring or ATS decision system.

## Run locally

1. Install Python 3.
2. Double-click `Start-RoleFit.bat` (Windows), or run `python rolefit_server.py` in this directory.
3. Keep the server window open. Open `http://127.0.0.1:8765/rolefit-ai.html` if your browser did not open automatically.
4. Paste text, browse for a resume, or drag a supported file onto the upload area. The first OCR/AI run needs internet to load the browser libraries and model; later runs are cached by the browser.

The server binds only to `127.0.0.1` and serves this folder. To stop it, press Ctrl+C in the terminal window.

## Supported resume files

- Text: `.txt`, `.md`, `.csv`
- Word: `.docx`
- PDF: text PDFs and image/scanned PDFs (OCR handles up to the first 8 scanned pages)
- Images: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`

The file picker intentionally shows all files so it does not hide resumes because of restrictive browser filters. RoleFit checks file signatures as well as extensions. Scanned/image resumes use Tesseract.js OCR; review the extracted text before matching because OCR can misread names, symbols, and technical terms. Old `.doc` files should be saved as `.docx` first.

## AI, scoring, and privacy

Transformers.js runs `Xenova/all-MiniLM-L6-v2` in the browser to create sentence embeddings. For each job requirement, the page displays the closest resume sentence and the semantic similarity. Explicit skill/phrase overlap also affects evidence retrieval and labels. The weighted evidence score awards 1 for a strong text match, 0.5 for related wording, and 0 for no clear wording match; explicit must/required/minimum/essential requirements carry extra weight.

Similarity is not probability, and the score is not accuracy or interview likelihood. Thresholds are demo values, the model is general-purpose English, and no labelled benchmark or fairness evaluation is included. Always inspect the evidence and only claim experience that is true.

Resume and job text are read and analyzed in the browser. They are not sent to an AI API or stored by the local server. The browser downloads the app's public JS libraries and model/OCR assets from CDNs; first use needs internet. The production version should pin and self-host dependencies if reproducible supply-chain control is required.

## Project files

- `rolefit-ai.html` — app UI and browser-side analysis.
- `rolefit_server.py` — loopback-only local static server.
- `Start-RoleFit.bat` — Windows launcher.
- `rolefit-ai-project-guide.md` — architecture, demo speech, resume bullets, limitations.
- `rolefit-sample-resume.txt` and `rolefit-sample-job-description.txt` — fictional demo data.

Keep personal resumes and contact details out of this public repository.

## Deployment

The HTML app can be hosted as a static HTTPS site such as GitHub Pages. Static hosting is not configured or published yet; get the owner's review before pushing this folder to a public repository or deploying it.


## Deploy

This is a static, client-side app. The `index.html` file is the hosted entry point; `netlify.toml` configures the publish directory. Connect this repository to Netlify and deploy with no build command, or use the Netlify CLI from this folder. The private local launcher and sample files are for local use only.

The public site downloads its parser/OCR libraries and language model from public CDNs. Resume and job text remain in the visitor's browser; do not add personal resumes or credentials to this repository.
