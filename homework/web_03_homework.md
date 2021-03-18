# web_03_homework

> **Bootstrap**
>
> **Bootstrap Component**



## 1. Button

```html
<div class="d-grid gap-2 col-6 mx-auto">
  <button class="btn btn-success" type="button">Sign in</button>
</div>
```





___

## 2. Nav Bar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                프로젝트
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                그룹들
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">활동</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">마일스톤</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">스니펫</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
```





___

## 3. Pagination

```html
<nav aria-label="...">
    <ul class="pagination">
        <li class="page-item disabled">
            <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
        </li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active" aria-current="page">
            <a class="page-link" href="#">2</a>
        </li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item">
            <a class="page-link" href="#">Next</a>
        </li>
    </ul>
</nav>
```





___

## 4. Login Page

```html
<div class="alert alert-danger" role="alert">Invalid Login or Password.</div>
      <h1>SSAFY 전용 GitLab 시스템</h1>
      <hr>
      <form action="" class="border">
        <h3 class="text-center m-3">Sign in</h3>
        <div class="bg-primary m-3" style="height: 2px"></div>
        <!-- <hr class="bg-danger"> -->
        <div class="mb-3 mx-3">
          <label for="exampleFormControlInput1" style="font-weight: bold;" class="form-label">Username or Email</label>
          <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
        </div>
        <div class="mb-3 mx-3">
          <label for="exampleFormControlInput1" style="font-weight: bold;" class="form-label">Password</label>
          <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
        </div>
        <div class="form-check mx-3 d-flex justify-content-between">
          <div>
            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
            <label class="form-check-label" style="font-weight: bold;" for="flexCheckDefault">
              Rememeber me
            </label>
          </div>         
          <a href="" class="text-decoration-none">Forgot your password?</a>
        </div>
        <div class="d-grid gap-2 col-8 mx-auto m-3">
          <button class="btn btn-success" type="button">Sign in</button>
        </div>
      </form>
```





___

