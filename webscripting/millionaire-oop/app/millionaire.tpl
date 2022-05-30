<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <meta name="author" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>

    <title>Worksheet Webscripting 4 - Task 7 </title>
</head>
<body class="">
  <header class="bg-secondary p-3">
    <h1 class="display-6 text-center">Worksheet Webscripting 4 - Task 7 - Millionaire</h1>
  </header>
  <main class="container my-4">
 
  <form class="py-5" action="/" method="post">
      <h1 class="h3 mb-3 fw-normal">How long to become a Millionaire?</h1>

      <div class="form-floating">
        <input type="text" class="form-control" id="money" name="money" placeholder="0.0" value="{{money}}">
        <label for="money">Money</label>
      </div>

    <div class="my-3">
      <div class="form-check">
        <input class="form-check-input" type="radio" name="interestCharges" id="flexRadioDefault1" value="1.00" \\
          % if interestCharges == 1.01 or interestCharges == None: 
            checked\\
          % end
        >
        <label class="form-check-label" for="flexRadioDefault1">1.00&#37;</label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="interestCharges" id="flexRadioDefault2" value="2.00" \\
          % if interestCharges == 1.02: 
            checked\\
          % end
        >
        <label class="form-check-label" for="flexRadioDefault2">2.00&#37;</label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="interestCharges" id="flexRadioDefault3" value="5.00" \\
          % if interestCharges == 1.05: 
            checked\\
          % end
        >
        <label class="form-check-label" for="flexRadioDefault3">5.00&#37;</label>
      </div>
    </div>

    <div class="form-floating my-3">
      <input type="text" class="form-control disabled" id="result" name="result" placeholder="0.0" value="{{msg}}" disabled>
      <label for="result">Years</label>
    </div>

    <input type="submit" class="w-100 btn btn-lg btn-primary" value="Calculate">
  </form>

</main>
</body>
</html>