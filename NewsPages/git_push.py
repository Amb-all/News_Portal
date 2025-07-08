import subprocess
import os

def run_cmd(cmd):
    """Запуск shell-команды и возврат результата"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and "nothing to commit" not in result.stderr:
        print(result.stderr.strip())
    return result

def main():
    print("📁 Текущая директория:", os.getcwd())

    # Инициализация git-репозитория, если отсутствует
    if not os.path.exists(".git"):
        print("🧱 Git не инициализирован. Выполняем git init...")
        run_cmd("git init")

    # Запрос имени ветки
    branch = input("🌿 Введите имя ветки (по умолчанию 'main'): ").strip() or "main"

    # Переключение на указанную ветку
    print(f"➡ Переключаемся/создаём ветку '{branch}'...")
    run_cmd(f"git checkout -B {branch}")

    # Запрос ссылки на удалённый репозиторий
    remote_url = input("🔗 Введите ссылку на ваш GitHub-репозиторий (например, https://github.com/user/repo.git): ").strip()
    if not remote_url:
        print("❌ Ссылка не указана. Завершение.")
        return

    # Привязка удалённого репозитория
    run_cmd("git remote remove origin")  # Удалим старую ссылку, если была
    run_cmd(f"git remote add origin {remote_url}")

    # Добавление файлов и коммит
    print("📦 Добавляем файлы...")
    run_cmd("git add .")

    commit_message = input("📝 Введите сообщение коммита (по умолчанию 'Initial commit'): ").strip() or "Initial commit"
    run_cmd(f'git commit -m "{commit_message}"')

    # Push в выбранную ветку
    print(f"🚀 Пушим в ветку '{branch}'...")
    run_cmd(f"git push -u origin {branch}")

    print("✅ Успешно завершено!")

if __name__ == "__main__":
    main()
