import subprocess
import os

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result

def git_push(branch: str, remote_url: str, commit_message: str = "Initial commit"):
    print(f"\n🚀 Пушим в ветку '{branch}'...")

    # Проверка: нет ли конфликта имён из-за вложенных веток
    if "/" in branch:
        parts = branch.split("/")
        parent_branch = parts[0]
        check_parent = run_cmd(f"git show-ref --verify --quiet refs/heads/{parent_branch}")
        if check_parent.returncode == 0:
            print(f"❌ Ошибка: ветка '{parent_branch}' уже существует!'{branch}'.")
            print("💡 Переименуйте ветку, например: 'feature_news_pages' или удалите конфликтующую.")
            return

    # Привязка к удалённому репозиторию
    subprocess.run(f"git remote add origin {remote_url}", shell=True)

    # Добавление всех файлов
    subprocess.run("git add .", shell=True)

    # Коммит
    subprocess.run(f'git commit -m "{commit_message}"', shell=True)

    # Создание и переключение на новую ветку
    subprocess.run(f"git checkout -b {branch}", shell=True)

    # Push в удалённый репозиторий
    subprocess.run(f"git push -u origin {branch}", shell=True)

    print("✅ Готово.")

# Пример использования
def main():
    remote = input("🔗 Введите ссылку на ваш репозиторий (например https://github.com/user/repo.git): ").strip()
    branch = input("🌿 Введите имя новой ветки: ").strip()
    message = input("💬 Комментарий к коммиту [по умолчанию: Initial commit]: ").strip() or "Initial commit"

    git_push(branch, remote, message)


if __name__ == "__main__":
    main()
