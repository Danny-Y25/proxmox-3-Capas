import { UserModel } from './../models/user';
import { Component, OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import {ApiService} from '../../services/api.service'


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor(
    private _api : ApiService,
    private _auth: AuthService,
    private _route: ActivatedRoute,
    private router: Router,


  ) { }

  ngOnInit(): void {



    this.test_jwt()
  }

  test_jwt(){
    // console.log(b)
    // this._api.postTypeRequest('login', username).subscribe((res: any) => {
    //   console.log(res)
    //   console.log(res.data_user)
    //   if(res.access_token){
    //     this._auth.setDataInLocalStorage('token', res.access_token)
    //     this.router.navigate(['profile/'+res.data_user[3]+"/"+res.data_user[5]]);
    //   }
    // }, err => {
    //   console.log(err)
    // });
  }

  logOut(){
    console.log("salio")
    this._auth.clearStorage()
    this.router.navigate(['/login']);
  }
}
