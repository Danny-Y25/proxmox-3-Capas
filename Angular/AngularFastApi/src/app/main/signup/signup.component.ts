import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import {ApiService} from '../../services/api.service'

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  form!: FormGroup;

  constructor(
    private _api : ApiService,
    private _auth: AuthService,
    private router: Router,
    public fb: FormBuilder
  ) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      firstname: ['', Validators.required],
      lastname: ['', Validators.required],
      username: ['', Validators.required],
      country: ['', Validators.required],
      password_user: ['', Validators.required]

    });
  }

  signup(){
    let b = this.form.value
    console.log(b)
    this._api.postTypeRequest('dataProcessingA', b).subscribe((res: any) => {
      console.log(res)
      if(res){

        this.router.navigate(['login'])
      }
    }, err => {
      console.log(err)
    });
  }

}
