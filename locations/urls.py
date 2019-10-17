from django.urls import path

from .api import ApiCountryViewSet, ApiRegionViewSet, ApiProvinceViewSet, ApiCityViewSet, ApiProvincesByRegion, \
  ApiCitiesByProvince, ApiRegionsByCountry, ApiCityCoordinate

version = 'api/v1'

READ_ONLY = {
  'get': 'list'
}

urlpatterns = [
  path('api/regions_by_country', ApiRegionsByCountry.as_view(), name='regions_by_country'),
  path('api/provinces_by_region', ApiProvincesByRegion.as_view(), name='provinces_by_region'),
  path('api/cities_by_province', ApiCitiesByProvince.as_view(), name='cities_by_province'),
  path(f'{version}/coordinates/city', ApiCityCoordinate.as_view(), name='api_location_city_coordinates'),

  path(f'{version}/countries', ApiCountryViewSet.as_view(READ_ONLY), name='api_location_country_list'),
  path(f'{version}/regions', ApiRegionViewSet.as_view(READ_ONLY), name='api_location_region_list'),
  path(f'{version}/provinces', ApiProvinceViewSet.as_view(READ_ONLY), name='api_location_province_list'),
  path(f'{version}/cities', ApiCityViewSet.as_view(READ_ONLY), name='api_location_city_list'),
]
