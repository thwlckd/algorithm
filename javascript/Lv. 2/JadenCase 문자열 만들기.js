function solution(s) {
  const words = s.split(' ');

  return words
    .map((word) => {
      {
        if (word === '') return '';

        return word[0].toUpperCase() + word.slice(1).toLowerCase();
      }
    })
    .join(' ');
}
