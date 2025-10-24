
# retrieves the first image service of the first painting annotation
def get_image_service(canvas):
  if 'id' in canvas:
    first_painting_anno_page = canvas['items'][0]
    first_painting_anno = first_painting_anno_page['items'][0]
    first_painting_anno_body = first_painting_anno['body']
    # Handle Image API v3 or v2
    return first_painting_anno_body['service'][0].get('id') or first_painting_anno_body['service'][0].get('@id')
  else:
    first_painting_anno = canvas['images'][0]
    first_painting_anno_body = first_painting_anno['resource']
    if isinstance(first_painting_anno_body['service'], list):
      service = first_painting_anno_body['service'][0]
    else:
      service = first_painting_anno_body['service']
    # Handle Image API v3 or v2
    return service.get('@id')