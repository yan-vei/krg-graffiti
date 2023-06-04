export class Graffiti {
  constructor(
    public id: number,
    public address: string,
    public comment: string,
    public has_admin_checked: boolean,
    public image_url: string,
    public latitude: number,
    public longitude: number,
    public zip: number,
    public position: google.maps.LatLngLiteral,
    public infoContent: string
  ) {}
}
