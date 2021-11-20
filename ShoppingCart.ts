import { ​​​Product } from "../model/Product";
import { User } from "../model/User";

export class ShoppingCart{
    constructor(
        private _idCart: number,
        private _content: ​​​Product[],
    ) {
        this._idCart = _idCart;
        this._content = _content;
    }
}