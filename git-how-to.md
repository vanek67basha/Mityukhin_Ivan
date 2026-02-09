# Инструкция по работе с Git и GitHub

## Как создать SSH ключ
1. Откройте терминал
2. Выполните: `ssh-keygen -t ed25519 -C "ваш_email@example.com"`
3. Нажмите Enter для сохранения в папке по умолчанию
4. При желании введите пароль

## Как добавить ключ в аккаунт на GitHub
1. Скопируйте публичный ключ: `pbcopy < ~/.ssh/id_ed25519.pub`
2. На GitHub перейдите в Settings → SSH and GPG keys
3. Нажмите "New SSH key"
4. Вставьте ключ и сохраните

## Как склонировать репозиторий
1. Скопируйте SSH URL репозитория на GitHub
2. В терминале выполните: `git clone git@github.com:username/repository.git`
3. Перейдите в папку проекта: `cd repository`