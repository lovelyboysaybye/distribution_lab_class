#### PRESENTATION ABOUT IDEA AND PRINCIPE [Presentation.pdf](Presentation.pdf)
#### YOU CAN READ THE STRUCTURE OF FILES AND TEST HERE [classes_and_tests.md](classes_and_tests.md)
#### PLEASE, RUN [main.py](main.py) FOR VERIFYING ALL LOVELY BLOCKCHAIN CONCEPT (or you can find output here [main_output.md](main_output.md))
#### THANKS FOR AWESOME COURSE AND WORK :)


Платформа голосування.

Даний проєкт має на меті створення простої системи на базі технології blockchain, яка дозволить проводити онлайн
голосування на виборах студентського самоврядування університетів.
Оскільки студентське самоврядування університету підпорядковується законом про освіту і науку, то процес виборів 
членів студентського самоврядування потребує додаткової бюрократії, а саме:
* Збереження бюлетнів голосування протягом певного часу.
* Надання учасникам виборів можливості перевіряти процес підрахунку голосів (спостерігачі від кандидатів)
* Перевірку того, що людина є студентом даного факультету/університету і те, що її голос зараховано лише один раз.

Крім цього, результати підрахунку голосів не є "прозорим процесом", оскільки доступ до бюлетнів мають лише обмежене коло людей.
В час цифровізації та популяризації таких систем як Дія, створення системи прозорого голосування
 з доступом зі смартфону є актуальною.
Система голосування на базі технології блокчейн має два типи аккаунтів:
* Студент (blockchain_classes/account_class.py)
* Система Голосування (blockchain_classes/vote_system_account.py)

Система Голосування - це аккаунт, який дозволяє створити транзакції-бюлетні, які надсилаються наперед відомому списку студентів аккаунтів.
Дані транзакції-бюлетні, аккаунт студент повинен вказати як вхід своєї транзакції голосування, і надіслати їх назад Системі Голосування.
З допомогою спеціальних перевірок, транзакції бюлетні може витратити лише вказаний в них отримувач (студент). Крім цього,
дані бюлетні можна надіслати заповнені лише тій самій Системі Голосування, яка їх створила.

Така блокчейн система з двома типами аккаунтів (транзакцій), дозволяє створювати як голосування виборів студентів, так 
 і будь-які вільні голосування кожним студентом. Для того, щоб створити голосування потрібно лише знати список адрес-студентів,
 яким буде надано бюлетні для голосування.
У випадку університету, даний список може створюватись відповідно до подання старостами списку адрес своїх студентів.
Оскільки бюлетні буде збережено у системі блоків, то кожен студент перед виборами зможе перевірити, чи додали його аккаунт до цієї системи.

Згідно з законом про студентське самоврядування, кожен студент має право брати участь у вибору, тому при втраті доступу до старого
 аккаунту студента, він зможе створити нвоий і подати його адресу на вибори.

Система повинна складатись з:
* Аккаунту, який містить в собі: ПІБ, рік вступу, спеціальність.
* Створення опитування з специфічним ID.
* Доступ до створених блоків для підрахунку голосів з специфічного питання.

Потенційні проблеми (мінуси):
* Процес збирання адрес для голосування має бути максимально проконтрольований, оскільки зловмисник може створити декілька аккаунтів, і подати їх замість студентів.
 Можливий варіант запобіання цієї проблеми є викоирстання полів name, surname, student_id, які перед виборами будуть перевірятись згідн осписку всіх студентів університету.
 При існуванні однакових аккаунтів або неіснуючих студентів, такі аккаунти будуть вилучені зі списку бюлетнів і уточненні відповідними особами.
* Проблема анонімності. Хоч ID кожного аккаунту буде генеруватись випадковим чином, однак централізований деканат буде 
 містити базу даних якому студенту належить який аккаунт.

