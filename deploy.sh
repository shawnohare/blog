readonly PUBLISH_REPO="https://github.com/shawnohare/shawnohare.github.io"
readonly PUBLISH_DIR="shawnohare.github.io"
readonly GENERATOR_REPO_NAME="shawnohare.com"
readonly HUGO_PUBLIC_DIR="public"
readonly THEMES_DIR="themes"
readonly THEME_REPO="https://github.com/shawnohare/hugo-morphism"
readonly REV=$(git rev-parse HEAD)


if [[ -d "${PUBLISH_DIR}" ]]; then
  git clone "${PUBLISH_REPO}" "${PUBLISH_DIR}"
fi

if [[ -d "${THEMES_DIR}/${THEME_REPO}" ]]; then
  mkdir -p "${THEMES_DIR}"
  git clone "${THEME_REPO}" "${THEMES_DIR}/${THEME_REPO}"
fi

hugo -d "${HUGO_PUBLIC_DIR}"
cp -r "${HUGO_PUBLIC_DIR}/*" "${PUBLISH_DIR}"
cd "${PUBLISH_DIR}"
git add .
git commit -m "Generated from ${GENERATOR_REPO_NAME} commit ${REV}"
git push -f
cd ..



