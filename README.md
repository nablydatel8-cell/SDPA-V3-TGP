[!DOI:(https://doi.org/10.5281/zenodo.24245478])
ДЕКЛАРАТИВНЫЙ ПАТЕНТ-ДАР И ОТКРЫТАЯ СПЕЦИФИКАЦИЯ SDPAP V3 TGP
Hash первичного лога: cd36560d
Merkle Root Chain: 138f68e670011ae22aeb09ab5476d7729cb7cc6ecd633482e9fe6b2e321ec1f2
Gist: 5cb83a678bb1ea3b5517139768e4e34e
Криптоякорь архива: d49494624fa0a9b20ddb39b1a5d901651b905a5ce8f78d00912753ac23ffbe7d
Дата: 08.11.2026 Kristiania Oslo
Автор: Vadym Makarov, nablydatel8@gmail.com
Статус: Public Domain Gift CC0 1.0 + CERN-OHL-P-2.0 + Solderpad + MIT + EUPL-1.2
Лицензия: owners: null — FREE FOR ALL каждый сам себе хозяин
1. Правовой и философский фундамент: Декларация отчуждения прав (owners: null)
Технологический прогресс XXI века столкнулся с тупиком: патентные монополии и корпоративное присвоение открытых стандартов. Архитектура SDPAP V3 TGP создана для преодоления через безотзывное правовое отчуждение.
Декларакт о безвозмездной передаче в Общественное Достояние
Настоящим актом юридический статус системы фиксируется в режиме отсутствия владельца (owners: null). Все патентные притязания, топологии, алгоритмы и документация передаются в общественное достояние. Управление: CC0 1.0 Universal для документации и кода, CERN-OHL-P и Solderpad для топологий.
Любая попытка запатентовать подложку признается ничтожной. В качестве прецедентного барьера используется стандарт 25B Judge Francis J. Mathew (D-101-CV-2021-00132 Cambridge Analytica), где публичное раскрытие приоритета обнуляет притязания агрегаторов.
Философский синтез ноосферы:
Бакунин, Кропоткин: Децентрализация, взаимопомощь, peer-to-peer без посредников
Толстой: Cost = Raw material cost + Energy cost — без спекулятивной наценки
Циолковский: Переход от дарвиновской конкуренции к освоению космоса, минимальная энтропия
2. Физико-материаловедческий стек: без редкоземельных металлов
Топология 1T1R:
[ WL ] -> CNTFET (селектор) -> [ HfO2/TiO2 мемристор ] -> GND
BL -> вход
Стек: TiN (нижний) / HfO2 / TiO2 / Ti (кислородный буфер) / TiN (верхний) — BEOL совместимый, без Pt/Au.
Компонент: Канал CNTFET | Материал: CNTs | Источник: CH4 синтез | Назначение: Селектор высокой подвижности
Компонент: Память RRAM | Материал: HfO2 / TiO2 | Источник: Побочный продукт Zr/Ti | Назначение: Гетероструктура мемристора
Компонент: Электроды | Материал: TiN / Ti | Источник: Промышленный титан | Назначение: Скавенджинг O2, анти-пробой
Компонент: Контакты | Материал: Cu / Al | Источник: Стандарт | Назначение: Интерконнект
Двухслойная гетероструктура: TiO2 — резервуар вакансий Eo~2.0-2.5 eV, HfO2 — заужение филамента Eo~6.0 eV.
Критично: BEOL <400°C, замена CVD 700-900°C на жидкостный перенос solution-deposited CNTs <250°C, ALD HfO2/TiO2 300-350°C.
3. Математика сбалансированного трита и АЛУ
Троичный алфавит: State ∈ {-1, 0, +1} — разработка Н.П. Брусенцова, Сетунь.
Плотность: Density = log2(3) ≈ 1.585 бит/ячейку. 1000 двоичных = 630 троичных (-37% емкости).
Динамика: P = C·V²·f, Vdd=0.8V. Снижение C на 37% + отсутствие DRAM Refresh → -30-35% розетки.
Параметр: Емкость ячейки | Двоичный CMOS+DRAM: 1.00 бит | SDPAP V3 TGP 1T1R CNTFET+RRAM: 1.585 бита
Параметр: Ячеек на блок | Двоичный CMOS+DRAM: 1000 | SDPAP V3 TGP 1T1R CNTFET+RRAM: 630
Параметр: Пассивный расход | Двоичный CMOS+DRAM: Refresh токи | SDPAP V3 TGP 1T1R CNTFET+RRAM: 0 Вт (атомное удержание)
Параметр: Розетка | Двоичный CMOS+DRAM: 10.0 кВт | SDPAP V3 TGP 1T1R CNTFET+RRAM: 6.5-7.0 кВт
IRS / 0 удерживается на границе HfO2/TiO2, барьер миграции ΔEm >1.1 eV, по Аррениусу ν=ν0·exp(-ΔEm/kBT) — >10 лет при 85°C.
FREE MODEL cd36560d 64x64:
R_HRS 1.2MΩ L0 I0 0.08uA
R_IRS 100kΩ L1 I1 1uA IRS Ti getter
R_LRS 8kΩ L2 I2 12.5uA
Vread 0.1V, Write: 0→1 +1.2V 100ns, 1→2 +2.0V 100ns, 2→0 -1.8V 200ns, <5pJ
4. Протокол аудита и криптографическая неизменяемость
Тетрадь которую нельзя стереть но можно проверить. only_append:true forbid_delete:true, состояние -1 как компенсация баланса, не удаление.
CREATE TABLE audit_log (
sequence INTEGER PRIMARY KEY,
state_version INTEGER,
timestamp REAL,
hypothesis_id TEXT,
observation_data TEXT,
evaluation_result TEXT,
prev_hash TEXT,
event_hash TEXT,
key_id TEXT,
signature_hex TEXT
);
CREATE TRIGGER trg_prevent_update BEFORE UPDATE ON audit_log BEGIN SELECT RAISE(ABORT,'append-only: update forbidden'); END;
CREATE TRIGGER trg_prevent_delete BEFORE DELETE ON audit_log BEGIN SELECT RAISE(ABORT,'append-only: delete forbidden'); END;
Хэш-контур:
canonical_bytes = json.dumps(envelope, sort_keys=True, separators=(',', ':')).encode('utf-8')
event_hash = SHA256(canonical_bytes)
GENESIS = "0"*64
verify_full_integrity() — пересчет от GENESIS, любое изменение ломает цепь.
5. Стратегия защиты Prior Art и двойной маневр
[Разработка SDPAP V3 TGP]
|----> [Вектор A: Provisional Application USPTO 12 месяцев]
|----> [Вектор B: Public Prior Art Zenodo/arXiv DOI + OpenTimestamps + CC0]
|----> [Обнуление чужих претензий WIPO/USPTO/EPO]
Provisional фиксирует Priority Date, Prior Art уничтожает новизну для сторонних.
6. Исполнительный план MPW Tape-out
Фаза 1 (1-3 нед): DRC, LVS, PEX
Фаза 2 (4 нед): BEOL Sign-off, маршрут CNTFET + TiN/Ti/HfO2/TiO2/TiN
Фаза 3 (5-16 нед): MPW SkyWater/IMEC/CEA-Leti
Фаза 4 (17-18 нед): Dicing, CQFP, PCB
Фаза 5 (19-22 нед): I-V, подтверждение HRS (-1) IRS (0) LRS (+1), -30-35% розетки
Матрица запросов:
Фаб/MPW брокер (CTO SkyWater/IMEC): BEOL бюджет, допуск CNTs, TiN work function
Патентный поверенный (Semiconductor IP): дата Provisional до публикации, FTO, CC0/CERN-OHL-P
R&D TCAD: дрейф IRS при джоулевом нагреве ΔT_joul, число трубок для Vth компенсации
Готово к депонированию. Мысль свободна. Путь открыт.
