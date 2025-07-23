import subprocess
import webbrowser

def run_cmd(cmd):
    """Выполнить команду и вернуть результат с выводом."""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def git_push(branch: str, remote_url: str, commit_message: str = "Initial commit"):
    print(f"\n🚀 Пушим в ветку '{branch}'...")

    if "/" in branch:
        parts = branch.split("/")
        parent_branch = parts[0]
        check_parent = run_cmd(f"git show-ref --verify --quiet refs/heads/{parent_branch}")
        if check_parent.returncode == 0:
            print(f"❌ Ошибка: локальная ветка '{parent_branch}' уже существует и конфликтует с '{branch}'.")
            print("💡 Переименуйте ветку или удалите конфликтующую.")
            return False

    remotes = run_cmd("git remote")
    if "origin" not in remotes.stdout:
        add_remote = run_cmd(f"git remote add origin {remote_url}")
        if add_remote.returncode != 0:
            print(f"❌ Не удалось добавить удалённый репозиторий: {add_remote.stderr.strip()}")
            return False
        else:
            print("✅ Удалённый репозиторий 'origin' добавлен.")
    else:
        print("🔁 Удалённый репозиторий 'origin' уже существует.")

    add_result = run_cmd("git add .")
    if add_result.returncode != 0:
        print(f"❌ Ошибка при добавлении файлов: {add_result.stderr.strip()}")
        return False

    commit_result = run_cmd(f'git commit -m "{commit_message}"')
    if commit_result.returncode != 0:
        if "nothing to commit" in commit_result.stderr.lower() or "nothing to commit" in commit_result.stdout.lower():
            print("⚠️ Нет изменений для коммита.")
        else:
            print(f"❌ Ошибка при коммите: {commit_result.stderr.strip()}")
            return False
    else:
        print("✅ Коммит выполнен.")

    check_branch = run_cmd(f"git show-ref --verify --quiet refs/heads/{branch}")
    if check_branch.returncode == 0:
        checkout_result = run_cmd(f"git checkout {branch}")
        if checkout_result.returncode != 0:
            print(f"❌ Не удалось переключиться на ветку '{branch}': {checkout_result.stderr.strip()}")
            return False
        else:
            print(f"🔄 Переключились на существующую ветку '{branch}'.")
    else:
        checkout_result = run_cmd(f"git checkout -b {branch}")
        if checkout_result.returncode != 0:
            print(f"❌ Не удалось создать и переключиться на ветку '{branch}': {checkout_result.stderr.strip()}")
            return False
        else:
            print(f"✅ Создана и переключена на ветку '{branch}'.")

    push_result = run_cmd(f"git push -u origin {branch}")
    if push_result.returncode != 0:
        print(f"❌ Ошибка при push: {push_result.stderr.strip()}")
        return False

    print("✅ Готово. Изменения запушены.")
    return True

def main():
    remote = input("🔗 Введите ссылку на репозиторий (например https://github.com/user/repo.git): ").strip()

    print("🌐 Открываю репозиторий в браузере...")
    try:
        webbrowser.open(remote)
    except Exception as e:
        print(f"⚠️ Не удалось открыть браузер: {e}")

    branch = input("🌿 Введите имя новой ветки: ").strip()
    message = input("💬 Комментарий к коммиту [по умолчанию: Initial commit]: ").strip() or "Initial commit"

    success = git_push(branch, remote, message)

    if success:
        print("🌐 Открываю обновлённую страницу репозитория в браузере...")
        try:
            webbrowser.open(remote)
        except Exception as e:
            print(f"⚠️ Не удалось открыть браузер: {e}")

if __name__ == "__main__":
    main()
