def test_total():
    amounts = [100, 250, 75, 400]
    total = 0
    for a in amounts:
        total += a
    assert total == 825


def test_filter_pending():
    recs = [{"status": "Pending"}, {"status": "Approved"}, {"status": "Pending"}]
    pending = [r for r in recs if r["status"] == "Pending"]
    assert len(pending) == 2


def test_status():
    record = {"name": "Laptop", "status": "Pending"}
    record["status"] = "Approved"
    assert record["status"] == "Approved"


def test_dict_access():
    record = {"name": "Laptop", "amount": 1250.00}
    assert record["name"] == "Laptop"


def test_list_length():
    recs = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]
    assert len(recs) == 5
