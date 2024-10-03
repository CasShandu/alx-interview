export function taskFirst() {
  const task = 'I prefer const when I can.'; // Use const here
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let'; // Use let here
  combination += getLast();

  return combination;
}

