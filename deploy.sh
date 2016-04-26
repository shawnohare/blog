readonly publish_repo="https://github.com/shawnohare/shawnohare.github.io"
readonly public_dir="public"
readonly themes_dir="themes"
readonly themes_repo="https://github.com/shawnohare/hugo-morphism"
readonly theme="hugo-morphism"
readonly theme_path="${themes_dir}/${theme}"
readonly generator="shawnohare.com"
readonly rev=$(git rev-parse HEAD)
clean="false"


init() {
  echo "Initializing."
  if [[ "${clean}" == "true" ]]; then
    echo "Removing existing dirs."
    rm -rf "${public_dir}"
    rm -rf "${theme_path}"
  fi
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

build_site() {
  hugo --destination="${public_dir}"
  if [ $? -eq 0 ]; then 
    return 0 
  else 
    echo "Error building site.  Exiting."
    cleanup
    exit 1 
  fi
}



publish() {
  if [[ ! -d "${public_dir}" ]]; then
    echo "No site to publish!"
    cleanup
    exit 1
  fi

  cd "${public_dir}"
  git init
  git remote add origin "${publish_repo}" # this will fail
  git add .
  git commit -m "Generated from ${generator} commit ${rev}"
  git push -f --set-upstream origin master
  return 0
}

cleanup() {
  echo "Cleaning up."
}

main() {
  init
  get_theme
  build_site 
  publish
  cleanup
  return 0
}

for i in "$@"; do
  case $i in
    -c|--clean)
      echo "In clean mode.  Completely rebuilding site."
      clean=true
      shift
      ;;
    --default)
      echo "Default mode."
      shift
      ;;
    *)
      echo "Unknown option. Exiting"
      exit 1
      ;;
  esac
done

main


