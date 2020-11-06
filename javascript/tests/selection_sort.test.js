const selectionSort = require('../selection_sort');

function convert(input) {
  return JSON.stringify(selectionSort(input));
}

function makeString(input) {
  return JSON.stringify(input);
}

test('can handle an empty array', () => {
  expect(convert([])).toBe(makeString([]));
});

test('can sort one element', () => {
  expect(convert([5])).toBe(makeString([5]));
});

test('can sort two elements', () => {
  expect(convert([3, 1])).toBe(makeString([1, 3]));
});

test('can sort several elements', () => {
  expect(convert([10, 4, 3, 2, 1, 5])).toBe(makeString([1, 2, 3, 4, 5, 10]));
});
   
test('can sort negative and positive values', () => {
  expect(convert([-1, -2, 4, 2])).toBe(makeString([-2, -1, 2, 4]));
});

test('can sort an array containing repeating values', () => {
  expect(convert([1, 4, 2, 1, 2, 4, 20, -2])).toBe(makeString([1, 4, 2, 1, 2, 4, 20, -2].sort((a, b) => a - b)));
});

