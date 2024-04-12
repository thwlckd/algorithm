function solution(bookTime) {
  const sortedBookTime = bookTime.sort().map((book) =>
    book.map((time) => {
      const [hour, minute] = time.split(':');

      return Number(hour) * 60 + Number(minute);
    })
  );
  const rooms = [];
  let roomSize = 0;

  for (const [checkin, checkout] of sortedBookTime) {
    let isEmptyRoomExist = false;

    for (let i = 0; i < rooms.length; i++) {
      if (rooms[i] + 10 <= checkin) {
        rooms[i] = checkout;
        isEmptyRoomExist = true;
        break;
      }
    }

    if (!isEmptyRoomExist) {
      rooms.push(checkout);
      roomSize++;
    }
  }

  return roomSize;
}
