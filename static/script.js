const game = document.getElementById("game");
    const playbtn = document.getElementById("btn");
    game.style.display = "none";
    playbtn.addEventListener('click', function handleClick() {

      if (game.style.display === 'none') {
    game.style.display = 'block';

  }
    else if (game.style.display === 'block') {
    game.style.display = 'none';

  }

    });

    const one = document.getElementById("1");
    const c1 = document.getElementById("c1");
    one.style.display = "none";
    c1.addEventListener('click', function handleClick() {

      if (one.style.display === 'none') {
    one.style.display = 'block';

  }
    else if (one.style.display === 'block') {
    one.style.display = 'none';


  }

    });

    const kiss = document.getElementById("2_");
    const h2 = document.getElementById("h2");
    kiss.style.display = "none";
    h2.addEventListener('click', function handleClick() {

      if (kiss.style.display === 'none') {
    kiss.style.display = 'block';

  }
    else if (kiss.style.display === 'block'){
    kiss.style.display = 'none';


  }

    });

    const stay = document.getElementById("2");
    const h1 = document.getElementById("h1");
    stay.style.display = "none";
    h1.addEventListener('click', function handleClick() {

      if (stay.style.display === 'none') {
    stay.style.display = 'block';

  }
    else if (stay.style.display === 'block') {
    stay.style.display = 'none';


  }

    });

    let arrive = document.getElementById("arrive");
    const c2 = document.getElementById("c2");
    arrive.style.display = "none";
    c2.addEventListener('click', function handleClick() {

      if (arrive.style.display === 'none') {
    arrive.style.display = 'block';

  }
    else if (arrive.style.display === 'block') {
    arrive.style.display = 'none';


  }

    });
