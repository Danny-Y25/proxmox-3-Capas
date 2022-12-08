import { Component, Input,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { AuthService } from 'src/app/services/auth.service';
import { UserModel } from '../models/user';
import { Pipe } from '@angular/core';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  modeloUsuario: UserModel=new UserModel();
  listUser:any=[]
  constructor(
    private _api : ApiService,
    private _auth: AuthService,
    private router: Router,
  ) { }
  @Input() dep:any;
  ngOnInit(): void {
    console.log("ngOnInit");
    this.loadUsers();
  }

  loadUsers(){
    // this.listUser=this._api.getTypeRequest('list-users')
    // console.log(this.listUser)
    this._api.getTypeRequest('list-users').subscribe((res: any) => {
      console.log(res)
      if(res){
        this.listUser=Object.values(res)
        console.log("this.listUser")

        console.log(this.listUser)

      }
    }, err => {
      console.log(err)
    });
  }
}
