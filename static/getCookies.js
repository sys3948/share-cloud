function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      console.log(name.length);
      console.log(cookie);
      console.log(cookie.substring(0, name.length + 1))
      console.log(name);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        console.log('조건절에 잘 들어옴');
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
