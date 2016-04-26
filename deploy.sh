readonly publish_repo="https://github.com/shawnohare/shawnohare.github.io"
readonly publish_dir="shawnohare.github.io"
readonly generator="shawnohare.com"
readonly public_dir="public"
readonly themes_dir="themes"
readonly themes_repo="https://github.com/shawnohare/hugo-morphism"
readonly theme="hugo-morphism"
readonly theme_path="${themes_dir}/${theme}"
readonly rev=$(git rev-parse HEAD)


init() {
  # Clean public / publish dirs.
  rm -rf "${public_dir}"
  rm -rf "${publish_dir}"
  mkdir -p "${themes_dir}" "${publish_dir}"
  return 0
}

get_theme() {
  if [[ ! -d "${theme_path}" ]]; then
    git clone "${themes_repo}" "${theme_path}"
  else 
    # Update the theme.
    (cd "${theme_path}" && git pull)
  fi
  return 0
}

# publish copies the necessary files into a new directory that is force
# pushed to the appropriate GitHub Pages repo. This will completely overwrite
# the existing repo, so some caution is useful.
publish() {
  cp -r "$public_dir"/* "${publish_dir}"
  cp "CNAME" "${publish_dir}/CNAME"
  cd "${publish_dir}"
  git init
  git remote add origin "${publish_repo}"
  git add .
  git commit -m "Generated from ${generator} commit ${rev}"
  git push -f --set-upstream origin master
  return 0
}

main() {
  init
  get_theme
  publish
  return 0
}

main


