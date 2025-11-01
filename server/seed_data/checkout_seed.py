CHECKOUT_SEED = [
    # ---------- HISTORY (returned) ----------
    # Alice
    {
        "checkout_date": "2025-03-05T10:30:00",
        "due_date": "2025-03-19",
        "return_date": "2025-03-18T16:05:00",
        "email": "alice@example.com",
        "book_copy_serial": "978-0735211292-C-1",  # Atomic Habits
    },
    {
        "checkout_date": "2025-06-10T14:10:00",
        "due_date": "2025-06-24",
        "return_date": "2025-06-21T11:45:00",
        "email": "alice@example.com",
        "book_copy_serial": "978-0671027032-C-1",  # How to Win Friends
    },
    {
        "checkout_date": "2025-10-01T09:15:00",
        "due_date": "2025-10-15",
        "return_date": "2025-10-14T17:22:00",
        "email": "alice@example.com",
        "book_copy_serial": "978-1544512287-C-1",  # Can't Hurt Me
    },
    # Bob
    {
        "checkout_date": "2025-02-15T13:05:00",
        "due_date": "2025-03-01",
        "return_date": "2025-02-28T12:00:00",
        "email": "bob@example.com",
        "book_copy_serial": "978-1455586691-C-1",  # Deep Work
    },
    {
        "checkout_date": "2025-03-28T15:20:00",
        "due_date": "2025-04-11",
        "return_date": "2025-04-10T10:55:00",
        "email": "bob@example.com",
        "book_copy_serial": "978-0743269513-C-1",  # 7 Habits
    },
    {
        "checkout_date": "2025-07-22T11:40:00",
        "due_date": "2025-08-05",
        "return_date": "2025-08-01T09:10:00",
        "email": "bob@example.com",
        "book_copy_serial": "978-0071401944-C-1",  # Crucial Conversations
    },
    {
        "checkout_date": "2025-09-20T10:00:00",
        "due_date": "2025-10-04",
        "return_date": "2025-10-02T16:20:00",
        "email": "bob@example.com",
        "book_copy_serial": "978-0735211292-C-1",  # Atomic Habits (reused after Alice, non-overlap)
    },
    # Charlie
    {
        "checkout_date": "2025-04-11T09:45:00",
        "due_date": "2025-04-25",
        "return_date": "2025-04-24T15:00:00",
        "email": "charlie@example.com",
        "book_copy_serial": "978-1592858491-C-1",  # Gifts of Imperfection
    },
    {
        "checkout_date": "2025-06-30T12:10:00",
        "due_date": "2025-07-14",
        "return_date": "2025-07-12T14:42:00",
        "email": "charlie@example.com",
        "book_copy_serial": "978-0671027032-C-2",  # How to Win Friends
    },
    {
        "checkout_date": "2025-09-02T16:30:00",
        "due_date": "2025-09-16",
        "return_date": "2025-09-12T11:05:00",
        "email": "charlie@example.com",
        "book_copy_serial": "978-0307352156-C-1",  # Quiet
    },
    # Diana
    {
        "checkout_date": "2025-02-08T10:05:00",
        "due_date": "2025-02-22",
        "return_date": "2025-02-21T09:35:00",
        "email": "diana@example.com",
        "book_copy_serial": "978-0735211292-C-2",  # Atomic Habits
    },
    {
        "checkout_date": "2025-05-09T14:25:00",
        "due_date": "2025-05-23",
        "return_date": "2025-05-22T18:00:00",
        "email": "diana@example.com",
        "book_copy_serial": "978-1577314806-C-1",  # The Power of Now
    },
    {
        "checkout_date": "2025-08-14T08:55:00",
        "due_date": "2025-08-28",
        "return_date": "2025-08-26T13:40:00",
        "email": "diana@example.com",
        "book_copy_serial": "978-1591846444-C-1",  # Start With Why
    },
    # Ethan
    {
        "checkout_date": "2025-01-20T11:35:00",
        "due_date": "2025-02-03",
        "return_date": "2025-02-02T10:00:00",
        "email": "ethan@example.com",
        "book_copy_serial": "978-0804137386-C-1",  # Essentialism
    },
    {
        "checkout_date": "2025-07-01T09:20:00",
        "due_date": "2025-07-15",
        "return_date": "2025-07-13T16:10:00",
        "email": "ethan@example.com",
        "book_copy_serial": "978-0071401944-C-2",  # Crucial Conversations
    },
    {
        "checkout_date": "2025-10-05T13:45:00",
        "due_date": "2025-10-19",
        "return_date": "2025-10-18T15:30:00",
        "email": "ethan@example.com",
        "book_copy_serial": "978-0593538035-C-1",  # Never Finished
    },
    # ---------- CURRENT (no return_date) ----------
    # Ego Is the Enemy -> all 4 copies out to 4 users (Alice, Bob, Charlie, Diana)
    {
        "checkout_date": "2025-10-20T10:15:00",
        "due_date": "2025-11-10",
        "return_date": None,
        "email": "alice@example.com",
        "book_copy_serial": "978-1591847816-C-1",
    },
    {
        "checkout_date": "2025-10-21T11:00:00",
        "due_date": "2025-11-11",
        "return_date": None,
        "email": "bob@example.com",
        "book_copy_serial": "978-1591847816-C-2",
    },
    {
        "checkout_date": "2025-10-22T09:30:00",
        "due_date": "2025-11-12",
        "return_date": None,
        "email": "charlie@example.com",
        "book_copy_serial": "978-1591847816-C-3",
    },
    {
        "checkout_date": "2025-10-23T15:45:00",
        "due_date": "2025-11-13",
        "return_date": None,
        "email": "diana@example.com",
        "book_copy_serial": "978-1591847816-C-4",
    },
    # Ethan currently has a different title
    {
        "checkout_date": "2025-10-25T13:00:00",
        "due_date": "2025-11-08",
        "return_date": None,
        "email": "ethan@example.com",
        "book_copy_serial": "978-1455586691-C-2",  # Deep Work
    },
]
