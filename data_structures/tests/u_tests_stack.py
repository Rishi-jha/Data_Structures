import unittest
from data_structures.stack_n_queues import Stack

class StackUnitTests(unittest.TestCase):
    
    def test_stack_raises_stackoverflow_if_added_numbers_greater_than_max_limit(self):
        st = Stack.Stack(2)
        st.push(1)
        st.push(2)
        with self.assertRaisesRegex(RuntimeError, "StackOverFlow Exception: MAXSIZE of Stack: 2"):
            st.push(2)

    def test_stack_raises_underflow_error_if_poped_element_when_no_element_is_present(self):
        st = Stack.Stack()
        with self.assertRaisesRegex(RuntimeError, "UnderFlow Exception: No Elements in the Stack"):
            st.pop()
        st.push(1)
        st.push(2)
        st.pop()
        st.pop()
        with self.assertRaisesRegex(RuntimeError, "UnderFlow Exception: No Elements in the Stack"):
            st.pop()

    def test_stack_pop_returns_the_removed_element(self):
        st = Stack.Stack()
        st.push(1)
        self.assertEqual(1, st.pop())

    def test_stack_raises_value_error_if_negative_size_is_entered(self):
        with self.assertRaisesRegex(ValueError, "Size Could not be less than 1 if provided"):
            Stack.Stack(0)

    def test_stack_raises_last_inserted_when_peek_is_used(self):
        pass

    def test_return_when_is_empty_method_is_called_on_empty_stack(self):
        pass


if __name__ == '__main__':
    unittest.main()
