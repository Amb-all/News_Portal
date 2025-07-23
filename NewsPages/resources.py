from django.contrib.auth import get_user_model
from news.models import Author, Category, Post, Comment

User = get_user_model()

# Создание пользователей
user1 = User.objects.create_user(username='john_doe', password='1234')
user2 = User.objects.create_user(username='jane_smith', password='1234')

# Создание авторов
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Категории
cat1 = Category.objects.create(name='Политика')
cat2 = Category.objects.create(name='Образование')
cat3 = Category.objects.create(name='Спорт')
cat4 = Category.objects.create(name='Технологии')

# Посты
post1 = Post.objects.create(author=author1, post_type='AR', title='Политическая статья', content='Текст политической статьи...')
post2 = Post.objects.create(author=author2, post_type='AR', title='Образование сегодня', content='Текст статьи об образовании...')
post3 = Post.objects.create(author=author1, post_type='NW', title='Последние новости технологий', content='Новость о новых технологиях...')

post1.categories.add(cat1, cat2)
post2.categories.add(cat2)
post3.categories.add(cat3, cat4)

# Комментарии
comment1 = Comment.objects.create(post=post1, user=user2, text='Очень интересная статья!')
comment2 = Comment.objects.create(post=post1, user=user1, text='Спасибо за отзыв!')
comment3 = Comment.objects.create(post=post2, user=user1, text='Полностью согласен!')
comment4 = Comment.objects.create(post=post3, user=user2, text='Ого, крутая новость!')

# Лайки/дизлайки к постам
post1.like()
post1.like()
post2.like()
post3.dislike()

# Лайки/дизлайки к комментариям
comment1.like()
comment1.like()
comment2.dislike()
comment3.like()
comment4.like()
comment4.like()

# Обновление рейтингов авторов
author1.update_rating()
author2.update_rating()

# Лучший автор
best_author = Author.objects.order_by('-rating').first()
print(f"\nЛучший автор: {best_author.user.username}, рейтинг: {best_author.rating}")

# Лучшая статья
best_post = Post.objects.order_by('-rating').first()
print(f"\nЛучшая статья:")
print(f"Дата: {best_post.created_at}")
print(f"Автор: {best_post.author.user.username}")
print(f"Рейтинг: {best_post.rating}")
print(f"Заголовок: {best_post.title}")
print(f"Превью: {best_post.preview()}")

# Комментарии к лучшей статье
print("\nКомментарии к лучшей статье:")
for comment in best_post.comment_set.all():
    print(f"{comment.created_at} | {comment.user.username} | рейтинг: {comment.rating} | текст: {comment.text}")
