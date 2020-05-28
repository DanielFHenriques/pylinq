import pytest

from src.domain.list.linked_list import LinkedList


class TestLinkedList:

    @pytest.fixture
    def under_test(self):
        return LinkedList()

    def test_get__list_has_no_elements_returns_none(self, under_test):
        result = under_test.get(0)

        assert result is None

    def test_set__list_has_no_elements_returns_none(self, under_test):
        result = under_test.set(0, None)

        assert result is None

    def test_is_empty__list_has_no_elements__returns_true(self, under_test):
        result = under_test.is_empty()

        assert result is True

    def test_add__list_has_no_elements__returns_true(self, under_test):
        result = under_test.add(1)

        assert result is True

    def test_remove__list_has_no_elements__returns_false(self, under_test):
        result = under_test.remove(1)

        assert result is False

    def test_clear__list_has_no_elements__keeps_same_state(self, under_test):
        under_test.clear()

        assert under_test.is_empty()

    def test_to_array__list_has_no_elements__returns_empty_array(self, under_test):
        result = under_test.to_array()

        assert result == []

    def test_len__list_has_no_elements__returns_zero(self, under_test):
        result = len(under_test)

        assert result == 0

    def test_get__list_has_the_element__returns_it(self, under_test):
        expected = 1

        under_test.add(expected)

        actual = under_test.get(0)

        assert actual == expected

    def test_set__list_has_the_element__replaces_it(self, under_test):
        expected = 1

        under_test.add(expected)

        actual = under_test.set(0, 2)

        assert actual == expected

    def test_add__add_two_elements__get_preserved(self, under_test):
        under_test.add(1)
        actual = under_test.add(2)

        assert actual is True
        assert len(under_test) == 2
        assert under_test.to_array() == [1, 2]

    def test_remove__list_has_element__gets_removed(self, under_test):
        under_test.add(1)

        actual = under_test.remove(1)

        assert actual is True
        assert under_test.is_empty() is True
