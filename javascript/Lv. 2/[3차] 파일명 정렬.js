function solution(files) {
  const data = [];
  const numRegEx = /[0-9]{1,5}/;

  files.forEach((file) => {
    const num = file.match(numRegEx)[0];

    data.push({ file, head: file.split(num)[0], num: Number(num) });
  });

  data.sort((a, b) => {
    const fileA = a.head.toUpperCase();
    const fileB = b.head.toUpperCase();

    if (fileA === fileB) {
      return a.num - b.num;
    }

    if (fileA > fileB) return 1;
    else if (fileA < fileB) return -1;
    else return 0;
  });

  return data.map(({ file }) => file);
}

// 참고용 깔끔한 풀이
function solution(files) {
  return files.sort((a, b) => {
    const aHead = a.match(/^\D+/)[0].toLowerCase();
    const bHead = b.match(/^\D+/)[0].toLowerCase();

    if (aHead < bHead) return -1;
    if (aHead > bHead) return 1;

    const aNum = a.match(/\d+/)[0].replace(/^0+/, '');
    const bNum = b.match(/\d+/)[0].replace(/^0+/, '');

    return aNum - bNum;
  });
}
