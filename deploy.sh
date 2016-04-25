readonly publish_repo="https://github.com/shawnohare/shawnohare.github.io"
readonly publish_dir="shawnohare.github.io"
readonly generator="shawnohare.com"
readonly public_dir="public"
readonly themes_dir="themes"
readonly themes_repo="https://github.com/shawnohare/hugo-morphism"
readonly theme="hugo-morphism"
readonly theme_path="${themes_dir}/${theme}"
readonly rev=$(git rev-parse HEAD)


mkdir -p "${themes_dir}" 

if [[ ! -d "${publish_dir}" ]]; then
  git clone "${publish_repo}" "${publish_dir}"
fi

if [[ ! -d "${theme_path}" ]]; then
  git clone "${themes_repo}" "${theme_path}"
else 
  cd "${theme_path}"
  git pull
  cd ../..
fi

hugo -d "${public_dir}"
cp -r "${public_dir}"/* "${publish_dir}"
cd "${publish_dir}"
git add .
git commit -m "Generated from ${generator} commit ${rev}"
git push -f
cd ..



