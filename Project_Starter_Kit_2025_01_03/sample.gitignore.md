# Sample .gitignore File

## Setup Instructions
1. Rename this file from `sample.gitignore.md` to `.gitignore`
2. Save it to the root of your project directory
3. Customize the sections below based on your project's needs

> **Note:** This is a starter template. Feel free to add or remove entries to match your specific project requirements.

---

```gitignore
# ====================
# Environment & Credentials
# ====================
.env
.env.local
.env.*.local
.env.development
.env.production
.env.test
*.pem
*.key
*.crt
*.p12
*.pfx
credentials.json
secrets.json
config.secret.*
*.secret
.secrets/
api_keys.txt
oauth_tokens.json

# ====================
# macOS
# ====================
.DS_Store
.AppleDouble
.LSOverride
._*
.Spotlight-V100
.Trashes
Icon?
.fseventsd
.TemporaryItems
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# ====================
# Windows
# ====================
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db
*.stackdump
[Dd]esktop.ini
$RECYCLE.BIN/
*.lnk
*.cab
*.msi
*.msm
*.msp

# ====================
# Linux
# ====================
*~
.nfs*
.fuse_hidden*
.directory
.Trash-*

# ====================
# IDEs & Editors
# ====================
.idea/
.vscode/
*.swp
*.swo
*.swn
*.bak
*.orig
*~
.project
.classpath
.settings/
*.sublime-project
*.sublime-workspace
.spyproject/
.ropeproject/
.pydevproject
*.code-workspace

# ====================
# Build & Dependencies
# ====================
node_modules/
vendor/
bower_components/
dist/
build/
out/
target/
*.egg-info/
__pycache__/
*.pyc
*.pyo
.cache/
.parcel-cache/
.next/
.nuxt/
.output/

# ====================
# Log Files
# ====================
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# ====================
# Testing & Coverage
# ====================
coverage/
.nyc_output/
.coverage
htmlcov/
.pytest_cache/
.tox/

# ====================
# Miscellaneous
# ====================
*.tmp
*.temp
.tmp/
.temp/
*.bak
*.backup
```
