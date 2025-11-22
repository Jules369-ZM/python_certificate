from hash_table import HashTable

# Test the HashTable implementation
def test_hash_table():
    ht = HashTable()

    # Test 1: HashTable class exists
    assert hasattr(ht, 'collection')
    assert ht.collection == {}
    print("1. HashTable class with empty collection: PASS")

    # Test 2: hash method exists and works correctly
    assert hasattr(ht, 'hash')
    assert ht.hash('golf') == 424  # g=103, o=111, l=108, f=102
    print("2. Hash method returns 424 for 'golf': PASS")

    # Test 3: add method exists
    assert hasattr(ht, 'add')
    ht.add('golf', 'sport')
    assert ht.collection == {424: {'golf': 'sport'}}
    print("3. Add 'golf', 'sport' to collection: PASS")

    # Test 4: add handles collisions (dear and read both hash to 412)
    ht.add('dear', 'friend')
    ht.add('read', 'book')
    # d=100, e=101, a=97, r=114 = 412
    # r=114, e=101, a=97, d=100 = 412
    assert 412 in ht.collection
    assert ht.collection[412] == {'dear': 'friend', 'read': 'book'}
    print("4. Add 'dear', 'friend' and 'read', 'book': PASS")

    # Test 5: lookup method exists and works
    assert hasattr(ht, 'lookup')
    assert ht.lookup('golf') == 'sport'
    assert ht.lookup('dear') == 'friend'
    assert ht.lookup('nonexistent') is None
    print("5. Lookup returns correct values and None for missing keys: PASS")

    # Test 6: remove method exists
    assert hasattr(ht, 'remove')
    ht.remove('golf')
    assert ht.lookup('golf') is None
    assert 424 not in ht.collection or ht.collection[424] == {}
    print("6. Remove 'golf' successfully: PASS")

    # Test 7: remove doesn't raise error for nonexistent key
    ht.remove('nonexistent')
    print("7. Remove nonexistent key without error: PASS")

    # Test 8: collection handles multiple keys at same index correctly
    ht = HashTable()
    ht.add('fcc', 'coding')
    ht.add('cfc', 'chemical')
    # f=102, c=99, c=99 = 300
    # c=99, f=102, c=99 = 300
    assert ht.collection == {300: {'fcc': 'coding', 'cfc': 'chemical'}}
    print("8. Multiple keys with same hash stored correctly: PASS")

    # Test 9: lookup returns 'sport' for 'golf'
    ht = HashTable()
    ht.add('golf', 'sport')
    assert ht.lookup('golf') == 'sport'
    print("9. Lookup 'golf' returns 'sport': PASS")

    # Test 10: lookup returns None when key doesn't exist
    assert ht.lookup('nonexistent') is None
    print("10. Lookup nonexistent key returns None: PASS")

    # Test 11: remove called on nonexistent key doesn't affect collection
    ht = HashTable()
    ht.add('rose', 'flower')
    original_collection = ht.collection.copy()
    ht.remove('nonexistent')
    assert ht.collection == original_collection
    print("11. Remove nonexistent key doesn't change collection: PASS")

    print("\nAll tests passed! HashTable implementation is complete.")

if __name__ == "__main__":
    test_hash_table()
